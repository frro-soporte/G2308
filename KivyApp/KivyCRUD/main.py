import os
import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider
from kivy.utils import get_color_from_hex


Builder.load_file("app.kv")

class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

class BaseDeDatos:
    def __init__(self, nombre_db):
        self.conn = sqlite3.connect(nombre_db)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS personas
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT NOT NULL,
                                edad INTEGER NOT NULL,
                                sexo TEXT NOT NULL)''')
        self.conn.commit()

    def insertar_persona(self, persona):
        self.cursor.execute('''INSERT INTO personas (nombre, edad, sexo)
                               VALUES (?, ?, ?)''', (persona.nombre, persona.edad, persona.sexo))
        self.conn.commit()

    def actualizar_persona(self, persona):
        self.cursor.execute('''UPDATE personas
                               SET nombre=?, edad=?, sexo=?
                               WHERE id=?''', (persona.nombre, persona.edad, persona.sexo, persona.id))
        self.conn.commit()

    def eliminar_persona(self, id_persona):
        self.cursor.execute('''DELETE FROM personas WHERE id=?''', (id_persona,))
        self.conn.commit()

    def obtener_todas_las_personas(self):
        self.cursor.execute('''SELECT * FROM personas''')
        filas = self.cursor.fetchall()
        personas = []
        for fila in filas:
            persona = Persona(fila[1], fila[2], fila[3])
            persona.id = fila[0]
            personas.append(persona)
        return personas

class FormularioPersona(BoxLayout):
    def __init__(self, base_datos, lista_personas, **kwargs):
        super(FormularioPersona, self).__init__(**kwargs)
        self.base_datos = base_datos
        self.lista_personas = lista_personas

        self.orientation = 'vertical'
        self.spacing = 10

        # Nombre Input
        self.label_nombre = self.ids.label_nombre
        self.entrada_nombre = self.ids.entrada_nombre

        # Edad Input
        self.label_edad = self.ids.label_edad
        self.slider_edad = self.ids.slider_edad
        self.entrada_edad = self.ids.entrada_edad

        # Genero Input
        self.label_sexo = self.ids.label_sexo
        self.spinner_sexo = self.ids.spinner_sexo

        self.boton_guardar = self.ids.boton_guardar
        self.boton_guardar.bind(on_release=self.guardar_persona)

    def guardar_persona(self, *args):
        nombre = self.entrada_nombre.text
        edad = self.entrada_edad.text
        sexo = self.spinner_sexo.text
        try:
            id = self.id
        except:
            id = None

        print(sexo)
        if not nombre or not edad or sexo not in self.spinner_sexo.values:
            self.mostrar_popup_error('Por favor, completa todos los campos.')
            return

        if not nombre.replace(" ", "").isalpha():
            self.mostrar_popup_error('Por favor, ingresa un nombre válido.')
            return

        if int(edad) >= 150 or int(edad) <= 0:
            self.mostrar_popup_error('Por favor, ingresa una edad válida.')
            return

        persona = Persona(nombre, int(edad), sexo)

        # Si tiene id es porque existe la persona y hay que editarla
        if id:
            persona.id = id
            self.base_datos.actualizar_persona(persona)
        else:
            self.base_datos.insertar_persona(persona)

        self.lista_personas.actualizar_lista()

        self.entrada_nombre.text = ''
        self.entrada_edad.text = ''
        self.spinner_sexo.text = 'Género'

        self.mostrar_popup_exito('Persona guardada exitosamente.')

    def mostrar_popup_exito(self, mensaje):
        popup = Popup(title='Éxito',
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def mostrar_popup_error(self, mensaje):
        popup = Popup(title='Error',
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

class ListaPersonas(BoxLayout):
    def __init__(self, base_datos, **kwargs):
        super(ListaPersonas, self).__init__(**kwargs)
        self.base_datos = base_datos

        self.orientation = 'vertical'
        self.spacing = 10

        self.actualizar_lista()

    def actualizar_lista(self):
        self.clear_widgets()

        personas = self.base_datos.obtener_todas_las_personas()
        for persona in personas:
            fila = GridLayout(cols=5, size_hint=(1, None), height=30, spacing=10)

            etiqueta_persona = Label(text=f'Nombre: {persona.nombre}  |  Edad: {persona.edad}  |  Género: {persona.sexo}')
            fila.add_widget(etiqueta_persona)

            boton_editar = Button(text='Editar', size_hint=(0.2, 1), background_color=get_color_from_hex('#0000FF'))
            boton_editar.bind(on_release=lambda btn, persona=persona: self.editar_persona(persona))
            fila.add_widget(boton_editar)

            boton_eliminar = Button(text='Eliminar', size_hint=(0.2, 1), background_color=get_color_from_hex('#FF0000'))
            boton_eliminar.bind(on_release=lambda btn, id_persona=persona.id: self.eliminar_persona(id_persona))
            fila.add_widget(boton_eliminar)

            self.add_widget(fila)

    def editar_persona(self, persona):
        formulario = FormularioPersona(self.base_datos, self)
        formulario.entrada_nombre.text = persona.nombre
        formulario.entrada_edad.text = str(persona.edad)
        formulario.spinner_sexo.text = persona.sexo
        formulario.id = persona.id

        self.clear_widgets()
        self.add_widget(formulario)

    def eliminar_persona(self, id_persona):
        self.base_datos.eliminar_persona(id_persona)
        self.actualizar_lista()

class MainApp(App):
    def __init__(self, nombre_db, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.nombre_db = nombre_db

    def build(self):
        base_datos = BaseDeDatos(self.nombre_db)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Agrega el título
        titulo = Label(text='CRUD Personas - Slider - Spinner', font_size=24, bold=True, size_hint=(1, 0.2))
        layout.add_widget(titulo)

        lista_personas = ListaPersonas(base_datos)
        formulario = FormularioPersona(base_datos, lista_personas)

        layout.add_widget(formulario)
        layout.add_widget(lista_personas)

        return layout

if __name__ == '__main__':
    app = MainApp('personas.db')
    app.run()
