from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivy_garden.mapview import MapView

import requests
import json
import datetime
from datetime import date


#window size
Window.size  = (350,600)

class Card(MDCard):
    source = StringProperty()
    text = StringProperty()


class Screenone(MDScreen):
    #home
    pass

class Screentwo(MDScreen):
    #mapview
    pass

class Screenthree(MDScreen):
    #nofications
    pass

class Screenfour(MDScreen):
    #account
    pass


#APP
class HealthPlus(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        global screen_manager
        screen_manager = ScreenManager()
        
        screen_manager.add_widget(Builder.load_file("index.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv")) 
        screen_manager.add_widget(Builder.load_file("register.kv")) 
        return screen_manager
    
    def on_start(self):
        pass

    #login process
    def login_process(self,email,password,):
        # something here
        if password and email != "":
            try:
                #login user
                data=[]
                url = 'http://127.0.0.1:8000/api/login'
                response = requests.post(url,json={'username':email,'password':password})
                data = response.json()
                with open('access.ini','w') as file:
                    file.write(data['token'])
                    file.close()                
                self.root.current = "home"
            except:
                Snackbar(
                    text="Login failed,check network connection",
                    snackbar_x="10dp",
                    snackbar_y="10dp",
                    size_hint_y = .08,
                    size_hint_x = (Window.width - (dp(10) * 2)) / Window.width,
                    bg_color = "#e14c4ce1",
                    font_size = "12sp"
                ).open()
        else:
            Snackbar(
                    text="Email or password was not provided!!",
                    snackbar_x="10dp",
                    snackbar_y="10dp",
                    size_hint_y = .08,
                    size_hint_x = (Window.width - (dp(10) * 2)) / Window.width,
                    bg_color = "#e14c4ce1",
                    font_size = "12sp",
                ).open()

 
    #signup process
    def signup_process(self,email,national_id,phonenumber,dob,password,passcode):
        # something here
        if email and password and passcode != "":
            if password == passcode:
                try:
                    # create user 
                    data = []
                    url = 'http://127.0.0.1:8000/api/register'
                    response = requests.post(url,json={
                                                'email':email,
                                                'national_ID':national_id,
                                                'phone_number':phonenumber,
                                                'date_of_birth':dob,
                                                'password':password,})
                    data = response.json()
                    status = data['status'] 
                    if status == "success":             
                        self.root.current = "login"
                    else:
                        Snackbar(
                        text=response.text,
                        snackbar_x="10dp",
                        snackbar_y="10dp",
                        size_hint_y = .08,
                        size_hint_x = (Window.width - (dp(10) * 2)) / Window.width,
                        bg_color = "#e14c4ce1",
                        font_size = "12sp").open()
                        
                except:
                    Snackbar(
                    text="registration failed,network problem",
                    snackbar_x="10dp",
                    snackbar_y="10dp",
                    size_hint_y = .08,
                    size_hint_x = (Window.width - (dp(10) * 2)) / Window.width,
                    bg_color = "#e14c4ce1",
                    font_size = "12sp").open()
                    
            else:
                Snackbar(
                    text="password didnt match",
                    snackbar_x="10dp",
                    snackbar_y="10dp",
                    size_hint_y = .08,
                    size_hint_x = (Window.width - (dp(10) * 2)) / Window.width,
                    bg_color = "#e14c4ce1",
                    font_size = "12sp").open()
        else:
            Snackbar(
                    text="Either email or password was not provided",
                    snackbar_x="10dp",
                    snackbar_y="10dp",
                    size_hint_y = .08,
                    size_hint_x = (Window.width - (dp(10) * 2)) / Window.width,
                    bg_color = "#e14c4ce1",
                    font_size = "12sp").open()
        
    #hospital locations
    def get_location(self):
        pass

    #blood request alerts
    def get_alerts(self):
        pass

    #donor e-card
    def get_card_details(self):
        pass
    
   

if __name__ == "__main__":
    HealthPlus().run()