from kivy.uix.gridlayout import GridLayout
from kivymd.uix.list import IconRightWidget
from kivy.uix.textinput import Texture
from kivymd.uix.chip.chip import MDIcon
from kivy.uix.image import AsyncImage
from kivymd.uix.banner.banner import MDFlatButton
from kivymd.uix.expansionpanel.expansionpanel import ImageLeftWidget
from kivymd.uix.banner.banner import OneLineAvatarListItem
from kivymd.uix.pickers.datepicker.datepicker import MDTextField
from kivymd.uix.filemanager.filemanager import FitImage
from kivymd.uix.bottomsheet.bottomsheet import MDIconButton
from kivymd.uix.navigationdrawer.navigationdrawer import NavigationDrawerContentError
from kivymd.uix.card.card import MDRelativeLayout
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from kivy.uix.dropdown import ScrollView
from kivymd.uix.list import MDList
from kivymd.uix.pickers.colorpicker.colorpicker import MDTabs
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.loader import Loader
import cohere
from kivy.animation import Animation
from kivymd.toast import toast
import subprocess
from asyncio import run
import keyboard
from datetime import datetime
import asyncio
import subprocess
import requests
import time
import os
import random
import socketio
import threading
import subprocess
from firebase import firebase
firebase = firebase.FirebaseApplication("https://chat-app-d2935-default-rtdb.firebaseio.com/", None)
from kivy.core.audio import SoundLoader
import pygame
from kivymd.uix.toolbar import MDTopAppBar
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from pyDes import *
from kivy.uix.popup import Popup
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager,FadeTransition
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from io import BytesIO
from kivy.uix.image import Image as GIFImage
from PIL import Image
from kivy.utils import platform
import base64
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem, MDList, IconLeftWidget, TwoLineAvatarIconListItem
import json
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.scrollview import ScrollView
import requests
import os
import emoji


SERVER_URL = "http://192.168.250.50:5000" # Replace with actual IP

album_details_base_url = "https://www.jiosaavn.com/api.php?__call=content.getAlbumDetails&_format=json&cc=in&_marker=0%3F_marker=0&albumid="

lyrics_base_url = "https://www.jiosaavn.com/api.php?__call=lyrics.getLyrics&ctx=web6dot0&api_version=4&_format=json&_marker=0%3F_marker%3D0&lyrics_id="
    
search_base_url = "https://www.jiosaavn.com/api.php?__call=autocomplete.get&_format=json&_marker=0&cc=in&includeMetaTags=1&query="

homedata = "www.jiosaavn.com/api.php?_format=json&_marker=0&api_version=4&ctx=web6dot0__call=webapi.getLaunchData"

song_details_base_url = "https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in&_marker=0%3F_marker%3D0&_format=json&pids="
playlist_details_base_url = "https://www.jiosaavn.com/api.php?__call=webapi.get&token={}&type=playlist&p=1&n=20&includeMetaTags=0&ctx=web6dot0&api_version=4&_format=json&_marker=0"



KV = '''

#:import SliverToolbar __main__.SliverToolbar
#: import WipeTransition kivy.uix.screenmanager.WipeTransition
#: import get_color_from_hex kivy.utils.get_color_from_hex
#:import SliverTool __main__.SliverTool



MDFloatLayout:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager



            MDScreen:
                name: "home"
                
                MDRelativeLayout:
                    size_hint:.09,.11
                    pos_hint:{"center_x":.08,"center_y":.96}
                    radius:15
                    FitImage:
                        source:"topbarlogo.png"
                        size_hint: None,None 
                        size: "50dp","50dp"
                        
                MDRelativeLayout:
                    size_hint:.4,.11
                    pos_hint:{"center_x":.34,"center_y":.96}

                    MDLabel:
                        text: "Ghost Comm"
                        bold:True
                        font_size: "30sp"
                        font_name: "font.ttf"
                        pos_hint: {"center_x":.42,"center_Y":.98}

                MDRelativeLayout:
                    size_hint:.4,.11
                    pos_hint:{"center_x":.29,"center_y":.922}

                    MDLabel:
                        text: "version 1.2.0"
                        bold:True
                        font_size: "15sp"
                        theme_text_color: "Custom"
                        text_color: 13/255,223/255,147/255,1
                        pos_hint: {"center_x":.57,"center_Y":.51}

                MDRelativeLayout:
                    size_hint:.4,.11
                    pos_hint:{"center_x":.8,"center_y":.96}
                        
                    MDIconButton:
                        icon: "account"
                        pos_hint: {"center_x":.85,"center_Y":.5}

                MDRelativeLayout:
                    size_hint:.4,.11
                    pos_hint:{"center_x":.75,"center_y":.96}
                        
                    MDIconButton:
                        icon: "bell"
                        pos_hint: {"center_x":.85,"center_Y":.5}

                ScrollView:
                    size_hint:1,.88
                    MDBoxLayout:
                        orientation: "vertical"
                        size_hint_y: None
                        height: self.minimum_height
                        spacing: dp(10)
                        padding: dp(10)


                        MDCard:
                            size_hint: None, None
                            pos_hint:{"center_x":.5,"center_y": .84}
                            size_hint: 0.9,.08
                            elevation: 2
                            radius: [10,]
                            border_radius: 10

                            TextInput:
                                id: profile_search
                                hint_text: "Search Profile ..."
                                helper_text: "Please Enter Correct Username"
                                size_hint: .7,None
                                mode: "fill"
                                pos_hint:{"center_x": .45,"center_y": .5}
                                height: self.minimum_height
                                multiline: False
                                cursor_color: 0,0,0,1
                                cursor_width:"2sp"
                                background_color: 0,0,0,0
                                padding: 15
                                font_size: "18sp" 
                                normal_color: app.theme_cls.bg_light
                                color_active: app.theme_cls.bg_light
                                icon_left: "magnify"
                                foreground_color: app.theme_cls.secondary_text_color

                            MDIconButton:
                                id: clo
                                icon: "close"
                                pos_hint:{"center_x":.85,"center_y":.5}
                                on_release:app.clear()

                            MDIconButton:
                                icon: "magnify"
                                pos_hint:{"center_x":.85,"center_y":.5}

                        ScrollView:
                            do_scroll_x: True
                            do_scroll_y: False
                            size_hint_y: None
                            height: "100dp"

                            MDBoxLayout:
                                id: story_grid
                                orientation: "horizontal"
                                size_hint_x: None
                                width: self.minimum_width
                                spacing: dp(10)
                                padding: dp(10)
                                Image:
                                    source:"topbarlogo.png"
                                    size_hint: None,None
                                    size: "65dp", "65dp"

                                Image:
                                    source:"topbarlogo.png"
                                    size_hint: None,None
                                    size: "65dp", "65dp"

                                Image:
                                    source:"topbarlogo.png"
                                    size_hint: None,None
                                    size: "65dp", "65dp"

                                Image:
                                    source:"topbarlogo.png"
                                    size_hint: None,None
                                    size: "65dp", "65dp"

                                Image:
                                    source:"topbarlogo.png"
                                    size_hint: None,None
                                    size: "65dp", "65dp"

                                Image:
                                    source:"topbarlogo.png"
                                    size_hint: None,None
                                    size: "65dp", "65dp"

                                Image:
                                    source:"topbarlogo.png"
                                    size_hint: None,None
                                    size: "65dp", "65dp"

                                Image:
                                    source:"topbarlogo.png"
                                    size_hint: None,None
                                    size: "65dp", "65dp"

                
                        MDList:
                            divider: "Inset"
                            divider_color:1,1,1,1
                            radius: [25,0,0,0]
                            TwoLineAvatarIconListItem:
                                id:home_name
                                text: "Abhay"
                                secondary_text: "Secondary text here"
                                on_release:app.change()
                                ImageLeftWidget:
                                    id:home_image
                                    source: "https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="
                                    radius: 24

                                IconRightWidget:
                                    icon: 'dots-vertical'

                            TwoLineAvatarIconListItem:
                                id:home_name
                                text: "Abhay"
                                secondary_text: "Secondary text here"
                                on_release:app.change()
                                ImageLeftWidget:
                                    id:home_image
                                    source: "https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="
                                    radius: 24

                                IconRightWidget:
                                    icon: 'dots-vertical'

                    
                            TwoLineAvatarIconListItem:
                                id:home_name
                                text: "Abhay"
                                secondary_text: "Secondary text here"
                                on_release:app.change()
                                ImageLeftWidget:
                                    id:home_image
                                    source: "https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="
                                    radius: 24

                                IconRightWidget:
                                    icon: 'dots-vertical'

                            TwoLineAvatarIconListItem:
                                id:home_name
                                text: "Abhay"
                                secondary_text: "Secondary text here"
                                on_release:app.change()
                                ImageLeftWidget:
                                    id:home_image
                                    source: "https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="
                                    radius: 24

                                IconRightWidget:
                                    icon: 'dots-vertical'

                            TwoLineAvatarIconListItem:
                                id:home_name
                                text: "Abhay"
                                secondary_text: "Secondary text here"
                                on_release:app.change()
                                ImageLeftWidget:
                                    id:home_image
                                    source: "https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="
                                    radius: 24

                                IconRightWidget:
                                    icon: 'dots-vertical'

                            TwoLineAvatarIconListItem:
                                id:home_name
                                text: "Abhay"
                                secondary_text: "Secondary text here"
                                on_release:app.change()
                                ImageLeftWidget:
                                    id:home_image
                                    source: "https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="
                                    radius: 24

                                IconRightWidget:
                                    icon: 'dots-vertical'


                MDIconButton:
                    size_hint: None, None
                    icon_size:"50sp"
                    on_release:app.ai_screen()
                    pos_hint: {"center_x":.9,"center_y":.15}
                    FitImage:
                        source:"https://swisscognitive.ch/wp-content/uploads/2020/09/the-4-top-artificial-intelligence-trends-for-2021.jpeg"
                        radius:24


            MDScreen:
                name: "profile"

                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.1
                    pos_hint:{"center_x":.5,"center_y":.94}
                    radius:15

                    MDIconButton:
                        icon: "arrow-left"
                        pos_hint:{"center_x":.05,"center_y":.5}
                        on_release:app.back()

                    

                    MDLabel:
                        id:name
                        text: "Profile"
                        
                        size_hint: None, None
                        font_size:"20dp"
                        pos_hint:{"center_x":.5,"center_y":.5}               

                FitImage:
                    id: profile_pic
                    size_hint:None, None
                    size: "300dp","300dp"
                    source:""
                    radius:24
                    pos_hint:{"center_x":0.5,"center_y":0.5}

                MDFloatingActionButton:
                    icon: "pencil"
                    pos_hint:{"center_x":0.655,"center_y":0.298}
                    on_release:app.select_pic()
                

            MDScreen:
                name:"chat"

                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.1
                    pos_hint:{"center_x":.5,"center_y":.94}
                    radius:15

                    MDIconButton:
                        icon: "arrow-left"
                        pos_hint:{"center_x":.05,"center_y":.5}
                        on_release:app.back()

                    FitImage:
                        id: image
                        size_hint:.07,.7
                        radius:12
                        pos_hint:{"center_x":.13,"center_y":.5}
                        source:"https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="

                    MDLabel:
                        id:name
                        text: "Abhay"
                        bold:True
                        size_hint: None, None
                        font_size:"20dp"
                        pos_hint:{"center_x":.25,"center_y":.5}

                    MDCard:
                        id:song_card
                        size_hint: None, None
                        pos_hint:{"center_x":.75,"center_y": .5}
                        size_hint: 0.5,.95
                        elevation: 1.5
                        radius: [10,]
                        border_radius: 10
                        MDLabel:
                            id: song_lab
                            text: "Tum Kyu Chale"
                            font_size: "15dp"
                            pos_hint:{"center_x":.5,"center_y":.5}
                            halign:"left"
                            size_hint_x:None
                            shorten:False

                        MDIconButton:
                            icon: "step-backward"
                            pos_hint:{"center_x":.85,"center_y":.5}

                        MDIconButton:
                            icon: "music-box"
                            pos_hint:{"center_x":.9,"center_y":.5}
                            on_release:app.music()

                        MDIconButton:
                            icon: "step-forward"
                            pos_hint:{"center_x":.95,"center_y":.5}


                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.62
                    pos_hint:{"center_x":.5,"center_y":.56}
                    radius:15
                    MDBoxLayout:
                        orientation: "vertical"
                        padding: [0, 10, 0, 10]  # Add padding to top and bottom
                        ScrollView:
                            id:scroll_view
                            MDList:
                                id:chat_list

                MDRaisedButton:
                    id: reply_label
                    text: ""
                    size_hint_x: 0.3
                    opacity: 0
                    pos_hint:{"center_x":.75,"center_y":.2}
                    on_release: app.cancel_reply()


                MDLabel:
                    id:typing_label
                    text:""
                    pos_hint:{"center_x":.55,"center_y":.2}
            

                MDCard:
                    size_hint: None, None
                    pos_hint:{"center_x":.5,"center_y": .1}
                    size_hint: 0.9,.1
                    elevation: 1.5
                    radius: [10,]
                    border_radius: 10
                    MDIconButton:
                        icon: "sticker-emoji"
                        pos_hint:{"center_x":.05,"center_y":.5}

                    TextInput:
                        id: message_input
                        hint_text: "Type a message ..."
                        helper_text: "Please Enter a message"
                        size_hint: .7,None
                        mode: "fill"
                        pos_hint:{"center_x": .45,"center_y": .5}
                        height: self.minimum_height
                        multiline: False
                        cursor_color: 0,0,0,1
                        cursor_width:"2sp"
                        background_color: 0,0,0,0
                        padding: 15
                        on_text: app.on_typing()
                        font_size: "18sp" 
                        normal_color: app.theme_cls.bg_light
                        color_active: app.theme_cls.bg_light
                        icon_left: "magnify"
                        foreground_color: app.theme_cls.secondary_text_color

                    MDIconButton:
                        id: close
                        icon: "close"
                        pos_hint:{"center_x":.85,"center_y":.5}
                        on_release:app.clear()

                    MDIconButton:
                        icon: "attachment"
                        pos_hint:{"center_x":.85,"center_y":.5}
                        on_release:app.file_manager_open()

                    MDIconButton:
                        icon: "send"
                        pos_hint:{"center_x":.95,"center_y":.5}
                        on_release: app.send_message()


            MDScreen:
                name:"music"
                ScrollView:
                    do_scroll_x:True
                    do_scroll_y:False
                    MDBoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: "90dp"
                        MDFlatButton:
                            text:"Trending Song"
                            bold: True
                            on_release:app.trend()

                        MDFlatButton:
                            text:"Bhojpuri Song"
                            bold: True
                            on_release:app.bhojpuri()

                        MDFlatButton:
                            text:"Romantic Song"
                            bold: True
                            on_release:app.romantic()

                        MDFlatButton:
                            text:"Party Song"
                            bold: True
                            on_release:app.party()

                        MDFlatButton:
                            text:"Old Song"
                            bold: True
                            on_release:app.old()

                MDLabel:
                    id: home_text
                    text: "Song is Searching ...."
                    pos_hint: {'center_x': .55, 'center_y': .5}
                    bold:True

                MDSpinner:
                    id: music_spinner
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    active: False

                ScrollView:
                    size_hint_y:.85
                    MDList:
                        id:home_music

                

                

                MDIconButton:
                    icon: "arrow-left"
                    pos_hint:{"center_x": .05,"center_y": .95}
                    md_bg_color: 1,1,1,1
                    on_release: app.c()

                MDCard:
                    size_hint: None, None
                    pos_hint:{"center_x":.5,"center_y": .95}
                    size_hint: 0.8,0.06
                    elevation: 2
                    radius: [10,]
                    border_radius: 10
                        
                    TextInput:
                        id: song_name
                        hint_text: "Songs, artists or podcasts"
                        helper_text: "Enter song name here"
                        size_hint: .9,None
                        pos_hint:{"center_x": .2,"center_y": .5}
                        height: self.minimum_height
                        multiline: False
                        cursor_color: 0,0,0,1
                        cursor_width:"2sp"
                        background_color: 0,0,0,0
                        padding: 15
                        font_size: "18sp" 
                        normal_color: app.theme_cls.bg_light
                        color_active: app.theme_cls.bg_light
                        icon_left: "magnify"
                        foreground_color: app.theme_cls.secondary_text_color
                        
            
                
                    MDIconButton:
                        icon: "magnify"
                        pos_hint:{"center_x": .93,"center_y": .5}
                        on_release:
                            app.show_data(song_name.text)

                        


            MDScreen:
                name: "music_list"
                md_bg_color: 0,0,0,0.77
                        
                MDSliverAppbar:
                    max_height: "70dp"
                    toolbar_cls: SliverToolbar()
                    
                    MDSliverAppbarHeader:

                    MDSliverAppbarContent:
                        id: cont
                        orientation: "vertical"
                        padding: "12dp"
                        spacing: "12dp"
                        md_bg_color: 0,0,0,0.77
                        adaptive_height: True
                        
            # 
                    
                MDSpinner:
                    id: spinner
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    active: False
                    
            
                MDSpinner:
                    id: spinner
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    active: False

                MDIconButton:
                    icon: "arrow-left"
                    pos_hint:{"center_x": .05,"center_y": .95}
                    md_bg_color: 1,1,1,1
                    on_release: app.c()

            MDScreen:
                name: "ai"

                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.1
                    pos_hint:{"center_x":.5,"center_y":.94}
                    radius:15

                    MDIconButton:
                        icon: "arrow-left"
                        pos_hint:{"center_x":.05,"center_y":.5}
                        on_release:app.back()

                    FitImage:
                        id: image
                        size_hint:.07,.7
                        radius:12
                        pos_hint:{"center_x":.13,"center_y":.5}
                        source:"https://swisscognitive.ch/wp-content/uploads/2020/09/the-4-top-artificial-intelligence-trends-for-2021.jpeg"

                    MDLabel:
                        id:name
                        text: "A.I ChatBot"
                        size_hint: None, None
                        font_size:"20dp"
                        pos_hint:{"center_x":.5,"center_y":.5}

                    


                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.62
                    pos_hint:{"center_x":.5,"center_y":.56}
                    radius:15
                    MDBoxLayout:
                        orientation: "vertical"
                        padding: [0, 10, 0, 10]  # Add padding to top and bottom
                        ScrollView:
                            id:scroll_view_ai
                            MDList:
                                id:ai_list
                            
                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.1
                    pos_hint:{"center_x":.5,"center_y":.1}
                    radius:15

                    MDIconButton:
                        icon: "sticker-emoji"
                        pos_hint:{"center_x":.05,"center_y":.5}

                    MDTextField:
                        id:ai_message
                        hint_text:'Type message ...'
                        mode: "fill"
                        required:False
                        pos_hint:{'center_x':0.45, 'center_y':0.5}
                        size_hint_x:.7
                        width:dp(200)
					    multiline:True

                    MDIconButton:
                        icon: "attachment"
                        pos_hint:{"center_x":.85,"center_y":.5}
                        on_release:app.file_manager_open()

                    MDIconButton:
                        icon: "send"
                        pos_hint:{"center_x":.95,"center_y":.5}
                        on_release: app.send_message_ai()

                        


'''


class Tab(MDFloatLayout, MDTabsBase):
    pass


class abhay(TwoLineAvatarIconListItem):
    pass

class SliverTool(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.title = "My Music"

class SliverToolbar(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.title = "Results"

class Test(MDApp):

    global screen_manager
    screen_manager = ScreenManager()
    last_screen = []
    username = "Himanshu"
    scroll = "False"
    song_url = ""
    trend_song = ""
    bhojpuri_song = ""
    romantic_song = ""
    party_song = ""
    old_song = ""
    selected_message = None 

    def build(self):
        
        self.file_manager = MDFileManager(exit_manager=self.file_manager_close, select_path=self.upload_file)
        
        self.manager_open = False
        self.file = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )
        self.sio = socketio.Client()
        self.sio.connect("http://127.0.0.1:5000")
        self.sio.on("message", self.receive_message)
        self.sio.on("file_received", self.receive_file)
        self.sio.on("upload_progress", self.update_upload_progress)
        self.sio.on("typing", self.show_typing)
        self.sio.on("stopped_typing", self.hide_typing)
        self.sio.on("play_music", self.play_received_music)
        self.sio.on("delete_message", self.handle_delete_message)
        self.sio.on("edit_message", self.handle_edit_message)
        self.sio.on("reaction", self.update_reaction_ui)
        self.process = None
        self.title = "Ghost Comm - Silent.Stealthy.Secret" 
        self.icon = "topbarlogo.png"
        pygame.mixer.init()
        

        self.typing_timer = None
        return Builder.load_string(KV)
    
    
    def change_screen(self, screen, *args):
        if self.root.ids.screen_manager.current == 'home' or self.root.ids.screen_manager.current == "hl":
            try:
                pass
            except:
                pass
        if args:
            self.root.ids.screen_manager.transition.direction = args[0]
            if args[0] != 'right':
                self.last_screen.append(self.root.ids.screen_manager.current)
                
        else:
            self.root.ids.screen_manager.transition.direction = 'left'
            self.last_screen.append(self.root.ids.screen_manager.current)
        self.root.ids.screen_manager.current = screen

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard == 13:
            if self.root.ids.screen_manager.current == 'music':
                self.show_data(self.root.ids.song_name.text)
            else:
                pass
      
        if keyboard in (1001, 27):   
            if self.manager_open:
                self.file_manager.back()
            else:
                self.back_screen()
 
        return True
    
    def ai_screen(self):
        self.change_screen("ai")

    def change(self):
        self.change_screen("chat")

    def c(self):
        self.change_screen("chat")

    def music(self):
        self.change_screen("music")

    def show_data(self, query):
       # close_btn = MDFlatButton(text="Close", on_release=self.close_dialog)
        if query == '':
            self.dia = MDDialog(title="Invalid Name", text="Please enter a song name", size_hint=(0.7,1))
            self.dia.open()
            
        else:
            #self.trend()
          #  self.root.ids.screen_manager.transition = WipeTransition()
            self.change_screen('music_list')
            self.root.ids.cont.clear_widgets()
            
            self.root.ids.spinner.active = True
            req = UrlRequest(search_base_url+query.replace(' ','+'), self.show_list)


    def show_list(self, req, result):
        self.root.ids.song_name.text = ""
        self.search_data = json.loads(result.replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"))['songs']['data']
        
        
        for i in range(len(self.search_data)):
            print(self.search_data[i]["title"])
            
            self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
            
        
            
            lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),theme_text_color="Custom",text_color=(1,1,1,1), secondary_text=self.search_data[i]['more_info']['primary_artists'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"), secondary_theme_text_color="Custom",secondary_text_color=(220/255,86/255,219/255,0.74/1),on_press=lambda x,y=i: self.song_details(y))
            sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
            
            sl = FitImage(source=self.image_url, radius=20)
            
            sk.add_widget(sl)
            lst.add_widget(sk)
            
      
         
            self.root.ids.cont.add_widget(lst)
            
        self.root.ids.spinner.active = False

    def trend(self, *args):
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.trend_s, daemon=True).start()

    def trend_s(self):
        Clock.schedule_once(lambda dt: self.trend_so())

    def trend_so(self):
        self.root.ids.home_music.clear_widgets()
        if self.trend_song == "":

            response = requests.get(playlist_details_base_url.format("I3kvhipIy73uCJW60TJk1Q__")+"&lyrics=true")
            if response.status_code == 200:
                songs_json = response.text.encode().decode()
                songs_json = json.loads(songs_json)
                self.search_data = songs_json['list']
                self.trend_song = self.search_data

                for i in range(len(self.search_data)):
                    print(self.search_data[i]["title"])
                    
                    self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                    
                
                    
                    lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                    sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                    
                    sl = FitImage(source=self.image_url, radius=20)
                    
                    sk.add_widget(sl)
                    lst.add_widget(sk)
                    
            
                
                    self.root.ids.home_music.add_widget(lst)



        else:
            self.search_data = self.trend_song
            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)

        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""


    def bhojpuri(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.bhojpuri_s, daemon=True).start()

    def bhojpuri_s(self):
        Clock.schedule_once(lambda dt: self.bhojpuri_so())

    def bhojpuri_so(self):
        try:
            self.search_data = self.bhojpu
            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)

        except:

            response = requests.get(playlist_details_base_url.format("8c-UE,,iBhN8497ZNqIDKA__")+"&lyrics=true")
            if response.status_code == 200:
                songs_json = response.text.encode().decode()
                songs_json = json.loads(songs_json)
                self.search_data = songs_json['list']
                self.bhojpuri_song = self.search_data
                for i in range(len(self.search_data)):
                    print(self.search_data[i]["title"])
                    
                    self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                    
                
                    
                    lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                    sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                    
                    sl = FitImage(source=self.image_url, radius=20)
                    
                    sk.add_widget(sl)
                    lst.add_widget(sk)
                    
            
                
                    self.root.ids.home_music.add_widget(lst)

        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""

    def romantic(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.romantic_s, daemon=True).start()

    def romantic_s(self):
        Clock.schedule_once(lambda dt: self.romantic_so())

    def romantic_so(self):
        response = requests.get(playlist_details_base_url.format("SBKnUgjNeMIwkg5tVhI3fw__")+"&lyrics=true")
        if response.status_code == 200:
            songs_json = response.text.encode().decode()
            songs_json = json.loads(songs_json)
            self.search_data = songs_json['list']

            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)

        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""

    def party(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.party_s, daemon=True).start()

    def party_s(self):
        Clock.schedule_once(lambda dt: self.party_so())

    def party_so(self):
        response = requests.get(playlist_details_base_url.format("qVvfieICUY5ieSJqt9HmOQ__")+"&lyrics=true")
        if response.status_code == 200:
            songs_json = response.text.encode().decode()
            songs_json = json.loads(songs_json)
            self.search_data = songs_json['list']

            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)

        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""

    def old(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.old_s, daemon=True).start()

    def old_s(self):
        Clock.schedule_once(lambda dt: self.old_so())

    def old_so(self):
        response = requests.get(playlist_details_base_url.format("qaou266p,04va8qgomsMOw__")+"&lyrics=true")
        if response.status_code == 200:
            songs_json = response.text.encode().decode()
            songs_json = json.loads(songs_json)
            self.search_data = songs_json['list']

            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)
        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""
        

    def song_details(self,i):
        self.song_id = self.search_data[i]['id']
        song_name = self.search_data[i]["title"]
        # self.animate_song_title(song_name)
        self.fetch_thread = threading.Thread(target=self.fetch_details)
        self.fetch_thread.start()

    def animate_song_title(self, song_name):
        ak = self.root.ids.song_lab
        ak.text = song_name

        # Reset position to start the scrolling from right again
        ak.x = self.root.ids.song_card.width

        # Define animation to move from right to left
        anim = Animation(x=-ak.texture_size[0], duration=6)
        anim += Animation(x=self.root.ids.song_card.width, duration=0)  # Reset position instantly

        # Repeat the animation indefinitely
        anim.repeat = True
        anim.start()

    def fetch_details(self):

        print('started fetching details')
        data = json.loads(requests.get(song_details_base_url+self.song_id).text.replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"))[self.song_id]
        try:
            data['media_url'] = self.decrypt_url(data['encrypted_media_url'])
            if data['320kbps'] != "true":
                data['media_url'] = data['media_url'].replace(
                    "_320.mp4", "_160.mp4")
            data['media_preview_url'] = data['media_url'].replace(
                "_320.mp4", "_96_p.mp4").replace("_160.mp4", "_96_p.mp4").replace("//aac.", "//preview.")
        except KeyError or TypeError:
            url = data['media_preview_url']
            url = url.replace("preview", "aac")
            if data['320kbps'] == "true":
                url = url.replace("_96_p.mp4", "_320.mp4")
            else:
                url = url.replace("_96_p.mp4", "_160.mp4")
            data['media_url'] = url
        print(data['media_url'])

        self.song_url = data['media_url']

        print(self.song_url)
        self.sio.emit("play_music", {"url": self.song_url,"user":self.username})
        
        
        if self.process:
            self.stop_music()  # Stop any existing process

        # Start ffplay in the background
        self.process = subprocess.Popen(
            ["ffplay", "-nodisp", "-autoexit", self.song_url],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )





    def decrypt_url(self,url):
        des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0",
                        pad=None, padmode=PAD_PKCS5)
        enc_url = base64.b64decode(url.strip())
        dec_url = des_cipher.decrypt(enc_url, padmode=PAD_PKCS5).decode('utf-8')
        dec_url = dec_url.replace("_96.mp4", "_320.mp4")
        return dec_url

    def on_start(self):
        Clock.schedule_once(self.trend,1)
        Clock.schedule_interval(self.close_icon,.1)
    

    def close_icon(self, *args):
        if self.root.ids.message_input.text == "":
            self.root.ids.close.icon = ""

        else:
            self.root.ids.close.icon = "close"

        if self.root.ids.profile_search.text == "":
            self.root.ids.clo.icon = ""

        else:
            self.root.ids.clo.icon = "close"

    def send_message(self):
        msg = self.root.ids.message_input.text.strip()

        if msg:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            message_id = str(time.time()) 
            data = {
                "sender": self.username,
                "message_id": message_id,
                "message": msg,
                "reply_to": self.selected_message if self.selected_message else None,
                "time": current_time
            }
            self.sio.emit("message", data)  # Send to server
            self.selected_message = None  # Reset after sending
            self.root.ids.message_input.text = ""  # Clear input
            self.update_reply_ui(None)

    def receive_message(self,data):
        
        reply_to = data.get("reply_to", None)
        Clock.schedule_once(lambda dt: self.add_message_to_ui(data, reply_to))

    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))

    def file_manager_close(self, *args):
        self.file_manager.close()

    def upload_file(self, path):
        self.file_manager_close()
        filename = os.path.basename(path)
        file_size = os.path.getsize(path)
        chunk_size = 1024 * 10  # 10 KB per chunk
        total_chunks = (file_size + chunk_size - 1) // chunk_size

        with open(path, "rb") as f:
            for chunk_index in range(total_chunks):
                chunk_data = f.read(chunk_size)
                self.sio.emit("file_chunk", {
                    "filename": filename,
                    "chunk": chunk_data,
                    "chunk_index": chunk_index,
                    "total_chunks": total_chunks
                })
        
        # Show upload progress in UI
        Clock.schedule_once(lambda dt: self.show_upload_progress(filename))

    def show_upload_progress(self, filename):
        progress_bar = MDProgressBar(value=0, max=100)
        progress_item = OneLineAvatarIconListItem(text=f"Uploading {filename}...")
        progress_item.add_widget(progress_bar)
        self.root.ids.chat_list.add_widget(progress_item)
        setattr(self, f"upload_progress_{filename}", progress_bar)

    def back(self):
        self.change_screen("home")

    def add_file_to_ui(self, filename, file_url):
        file_item = OneLineAvatarIconListItem(text=f"{self.username} :{filename}")
        file_item.add_widget(IconLeftWidget(icon="download"))
        file_item.bind(on_release=lambda x: self.download_file(file_url, filename))
        self.root.ids.chat_list.add_widget(file_item)

    def update_upload_progress(self, data):
        filename = data["filename"]
        progress = data["progress"]
        
        if hasattr(self, f"upload_progress_{filename}"):
            Clock.schedule_once(lambda dt: setattr(getattr(self, f"upload_progress_{filename}"), "value", progress))
    
    def receive_file(self, data):
        filename = data["filename"]
        file_url = data["url"]
        
        Clock.schedule_once(lambda dt: self.add_file_to_ui(filename, file_url))

    def add_message_to_ui(self, data, reply_to=None):
        chat_list = self.root.ids.chat_list
        sender = data["sender"]
        message_id = data["message_id"]
        message = data["message"]
        current_time = data["time"]
        reactions = data.get("reactions", {})
        reply_to = data.get("reply_to", None)
        long_text = f"{sender}: {message}"
        ak = break_text(long_text, 75)
        
        bubble = MDCard(
            size_hint_x=None,  # Let width be dynamically set
            size_hint_y=None,
            adaptive_size=True,
            pos_hint={'center_x': 0.1,'center_y': 0.5},
            padding=[40, 11],
            radius=[10, 10, 10, 0],  # Rounded edges
            md_bg_color=(210/255,212/255,217/255,1),
            id=message_id 
        )

        

        bub = MDCard(
            size_hint_x=None,  # Let width be dynamically set
            size_hint_y=None,
            adaptive_size=True,
            
            padding=[40, 10],
            radius=[10, 10, 10, 0],  # Rounded edges
            md_bg_color=(0.2, 0.6, 1, 1),
            id=message_id 
        )

        label = MDLabel(
            text=ak,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            size_hint_y=None,
            adaptive_size=True,
        )

        label_time = MDLabel(
            text=current_time,
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            size_hint_y=None,
            adaptive_size=True,
        )

        def show_menu(instance):
            dropdown_menu.open()

       

        def delete_message_action():
            self.delete_message(message_id)
            dropdown_menu.dismiss()

        def reply_message_action():
            self.select_message(message)
            dropdown_menu.dismiss()

        def copy_message_action():
            Clipboard.copy(message)
            toast("Message is copied.")
            dropdown_menu.dismiss()

        def reaction_message_action():
            self.show_reaction_menu(message_id)
            dropdown_menu.dismiss()

        menu_items = [
            {"text": "Delete", "on_release": delete_message_action},
            {"text": "Reply", "on_release": reply_message_action},
            {"text": "Copy", "on_release": copy_message_action},
            {"text": "Reaction", "on_release": reaction_message_action}
        ]

        if sender == self.username:
            def edit_message_action():
                self.show_edit_popup(message_id, message, sender)
                dropdown_menu.dismiss()
            menu_items.insert(0, {"text": "Edit", "on_release": edit_message_action})

        dropdown_menu = MDDropdownMenu(
            caller=bub,
            items=menu_items,
            width_mult=3
        )

        bub.bind(on_release=show_menu)
        bub.add_widget(label)
        bubble.add_widget(bub)
        bubble.add_widget(label_time)

        if reply_to:
            reply_bubble = MDCard(
                size_hint_x=None,
                size_hint_y=None,
                adaptive_size=True,
                padding=[15, 5],
                radius=[10, 10, 10, 10],
                md_bg_color=(0.5, 0.5, 0.5, 1)  # Gray for reply
            )
            reply_label = MDLabel(
                text=f"Replying to: {reply_to}",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                size_hint_y=None,
                adaptive_size=True,
            )
            reply_bubble.add_widget(reply_label)
            bubble.add_widget(reply_bubble)

        
        chat_list.add_widget(bubble)

    def show_reaction_menu(self, message_id):
        emoji_text = emoji.emojize(":orange_heart:")
        emoji_options = ["❤️", "😂", "👍", "🔥", "😢", "😮"]
    
    # Create reaction buttons dynamically
        reaction_buttons = [
            MDRaisedButton(text=emoji, on_release=lambda x, e=emoji: self.send_reaction(message_id, e))
            for emoji in emoji_options
        ]

        reaction_dialog = MDDialog(
            title="React to Message",
            buttons=reaction_buttons + [MDRaisedButton(text="Cancel", on_release=lambda x: reaction_dialog.dismiss())]
        )

        reaction_dialog.open()


    def update_reaction_ui(self, data):
        message_id = data["message_id"]
        reactions = data["reactions"]

        chat_list = self.root.ids.chat_list
        for widget in chat_list.children:
            if hasattr(widget, "id") and widget.id == message_id:
                for child in widget.children:
                    if isinstance(child, MDLabel):  # Find the reaction label
                        child.text = "".join([f"{emoji} {count} " for emoji, count in reactions.items()])
                        return


    def send_reaction(self, message_id, reaction):
        self.sio.emit("reaction", {"message_id": message_id, "reaction": reaction, "user": self.username})


    


    def show_edit_popup(self, message_id, old_message, sender):
        
        """Open a popup to edit a message."""
        content = MDBoxLayout(orientation='vertical', spacing=10, padding=10)

        text_input = MDTextField(
            text=old_message,
            hint_text="Edit your message..."
        )
        content.add_widget(text_input)

        save_button = MDRaisedButton(
            text="Save",
            on_release=lambda x: self.edit_message(message_id, text_input.text,sender)
        )
        content.add_widget(save_button)

        self.edit_popup = Popup(
            title="Edit Message",
            content=content,
            size_hint=(None, None),
            size=("400dp", "200dp"),
            background_color=(1,1,1,1)
        )
        self.edit_popup.open()

    def edit_message(self, message_id, new_message, sender):
        print("pressed")
        """Send an edit request to the server."""
        self.sio.emit("edit_message", {"message_id": message_id, "new_message": new_message, "user": sender})
        self.edit_popup.dismiss()

        #self.update_message_in(message_id, new_message)

    def handle_edit_message(self, data):
        """Handle an edited message from the server."""
        message_id = data["message_id"]
        new_message = data["new_message"]
        user = data["user"]
        Clock.schedule_once(lambda dt: self.update_message_in(message_id, new_message, user))

    def update_message_in(self, message_id, new_message, user):
        chat_list = self.root.ids.chat_list
        for widget in chat_list.children:
            if hasattr(widget, "id") and widget.id == message_id:
                for child in widget.children:
                    if isinstance(child, MDCard):  # 🔄 Check if message is inside an extra MDCard
                        for subchild in child.children:
                            if isinstance(subchild, MDLabel):
                                subchild.text = f"{user}: {new_message}"
                                return

    def delete_message(self, message_id):
        """Send delete request to the server and remove the message from UI."""
        self.sio.emit("delete_message", {"message_id": message_id})
        self.remove_message_from_ui(message_id)
        print("delete")
        
    def handle_delete_message(self, data):
        """Handle message deletion from the server."""
        message_id = data["message_id"]
        Clock.schedule_once(lambda dt: self.remove_message_from_ui(message_id))

    def remove_message_from_ui(self, message_id):
        """Find and remove the message from the UI."""
        chat_list = self.root.ids.chat_list
        for widget in chat_list.children[:]:  
            if hasattr(widget, "id") and widget.id == message_id:
                chat_list.remove_widget(widget)
                break

    def select_message(self, message):
        """Selects a message to reply to."""
        self.selected_message = message
        self.update_reply_ui(message)
        

    def update_reply_ui(self, message):
        """Updates the UI to show the selected message for reply."""
        reply_label = self.root.ids.reply_label

        if message:
            reply_label.text = f"Replying to: {message}"
            reply_label.opacity = 1
        else:
            reply_label.text = ""
            reply_label.opacity = 0

    def cancel_reply(self):
        """Cancels reply mode"""
        self.selected_message = None
        self.update_reply_ui(None)
      

    # def on_start(self):
    #     Clock.schedule_interval(self.up, 2)

    # def up(self, *args):
    #     self.root.ids.scroll_view.scroll_y = 0

    def download_file(self, url, filename):
        # Show download progress in UI
        Clock.schedule_once(lambda dt: self.show_download_progress(filename))

        # Start downloading in a separate thread
        threading.Thread(target=self.download_file_thread, args=(url, filename)).start()

    def show_download_progress(self, filename):
        progress_bar = MDProgressBar(value=0, max=100)
        progress_item = OneLineAvatarIconListItem(text=f"Downloading {filename}...")
        progress_item.add_widget(progress_bar)
        self.root.ids.chat_list.add_widget(progress_item)
        setattr(self, f"download_progress_{filename}", progress_bar)

    def download_file_thread(self, url, filename):
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        save_path = os.path.join(os.path.expanduser("~"), filename)

        with open(save_path, "wb") as f:
            downloaded_size = 0
            for chunk in response.iter_content(1024):
                if chunk:
                    f.write(chunk)
                    downloaded_size += len(chunk)
                    progress = (downloaded_size / total_size) * 100
                    Clock.schedule_once(lambda dt: self.update_download_progress(filename, progress))

        Clock.schedule_once(lambda dt: self.download_complete(filename, save_path))

    def update_download_progress(self, filename, progress):
        if hasattr(self, f"download_progress_{filename}"):
            progress_bar = getattr(self, f"download_progress_{filename}")
            progress_bar.value = progress

    def download_complete(self, filename, save_path):
        # Remove progress bar and show downloaded file
        Clock.schedule_once(lambda dt: self.replace_download_progress(filename, save_path))

    def replace_download_progress(self, filename, save_path):
        file_item = OneLineAvatarIconListItem(text=f"✅ {filename} (Downloaded)")
        file_item.add_widget(IconLeftWidget(icon="folder"))
        file_item.bind(on_release=lambda x: Clipboard.copy(save_path))
        self.root.ids.chat_list.add_widget(file_item)
        MDDialog(text=f"File saved: {save_path} (Path copied to clipboard)").open()

    def on_typing(self):
        """ Detects user typing and notifies others """
        
        self.sio.emit("typing", {"user": self.username})

        # Cancel any previous timer and restart it
        if self.typing_timer:
            self.typing_timer.cancel()
        self.typing_timer = Clock.schedule_once(self.user_stopped_typing, 2)


    def user_stopped_typing(self, dt):
        """ Called when user stops typing for 2 seconds """
        self.sio.emit("stopped_typing", {"user": self.username})

    def show_typing(self, data):
        """ Show 'User is typing...' only if another user is typing """
        if data["user"] != self.username:  # Avoid showing own typing status
            Clock.schedule_once(lambda dt: setattr(
                self.root.ids.typing_label, 'text', f"{data['user']} is typing..."
            ))

    def hide_typing(self, data):
        """ Hide 'User is typing...' when typing stops """
        if data["user"] != self.username:  # Ensure only other's typing is hidden
            Clock.schedule_once(lambda dt: setattr(self.root.ids.typing_label, 'text', ""))

    # def play_music(self, song_url):
    #     """ Sends song URL to all users """
    #     self.sio.emit("play_music", {"url": self.song_url})
        #os.system(f'ffplay -nodisp -autoexit "{self.song_url}"')

    def play_received_music(self, data):
        """ Plays music when received from another user """
        user = data.get("user")
         # Ensure only other's music is played
        if user == self.username:
            print("True")

        else:
            song_url = data.get("url", "")
            print(song_url)
            if self.process:
                self.stop_music()  # Stop any existing process

            # Start ffplay in the background
            self.process = subprocess.Popen(
                ["ffplay", "-nodisp", "-autoexit", song_url],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )

        #os.system(f'ffplay -nodisp -autoexit "{song_url}"')

    def stop_music(self):
        """Stops the currently playing music."""
        if self.process:
            self.process.terminate()  # Kill ffplay process
            self.process = None
            print("Stopped.")

    def profile_screen(self):
        self.change_screen("profile")

    def select_pic(self):
        self.file.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def select_path(self, path: str):
        self.exit_manager()
        
        try:
            re = firebase.delete("chat-app-d2935-default-rtdb/user/prfile", "")
        except:
            pass
        with open(path, "rb") as image_file:
            image_bytes = image_file.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        image_json = json.dumps(image_base64)
        data = {
            "image": image_json
        }

        ak = firebase.post("chat-app-d2935-default-rtdb/user/prfile",data)
        
        res = firebase.get("chat-app-d2935-default-rtdb/user/prfile", "")
        for i in res.keys():
            ak = res[i]["image"]

            image_data = json.loads(ak)
            image_bytes = base64.b64decode(image_data)
            image = Image.open(BytesIO(image_bytes))
            print(image_bytes)
            self.pro()
            image.save("profile.jpg")
            self.root.ids.profile_pic.source = ""
            self.root.ids.profile_pic.source = "profile.jpg"
                

            
        print(path)

    def pro(self):
        os.remove("profile.jpg")

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file.close()

    def send_message_ai(self):
        Query = self.root.ids.ai_message.text
        chat_list = self.root.ids.ai_list
        bubble = MDCard(
            size_hint_x=None,  # Let width be dynamically set
            size_hint_y=None,
            adaptive_size=True,
            pos_hint={'center_x': 0.1,'center_y': 0.5},
            padding=[40, 11],
            radius=[10, 10, 10, 0],  # Rounded edges
            md_bg_color=(210/255,212/255,217/255,1)  # Light blue
        )

        bub = MDCard(
            size_hint_x=None,  # Let width be dynamically set
            size_hint_y=None,
            adaptive_size=True,
            padding=[40, 10],
            radius=[10, 10, 10, 0],  # Rounded edges
            md_bg_color=(0.2, 0.6, 1, 1)  # Light blue
        )

        label = MDLabel(
            text=f"{self.username}:{Query}",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            size_hint_y=None,
            adaptive_size=True,
        )
        bub.add_widget(label)

        bubble.add_widget(bub)
        chat_list.add_widget(bubble)
        self.root.ids.scroll_view_ai.scroll_y = 0
        threading.Thread(target=self.a_i, daemon=True).start()

    def a_i(self):
        pass

        
    def clear(self):
        self.root.ids.message_input.text = ""
        self.root.ids.profile_search.text = ""

def break_text(text, limit):
    return '\n'.join([text[i:i+limit] for i in range(0, len(text), limit)])

Test().run()
