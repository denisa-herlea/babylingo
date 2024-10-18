screen_helper = """
ScreenManager:
    LoginScreen:
    IntroScreen:
    RegisterScreen:
    WelcomeScreen:
    AddNewBabyScreen:
    ChooseBabyScreen:
    UpdateBabyScreen:
    HomeScreen:
    AccountScreen:




<IntroScreen>:
    name: 'Intro'
    MDLabel:
        text: ""
        theme_text_color: "Primary"
        halign: "center"
        font_style: "H6"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}

<LoginScreen>:
    name: 'Login'
    MDLabel:
        text: "Please log in to continue"
        theme_text_color: "Primary"
        halign: "center"
        font_style: "H6"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    MDTextField:
        id: login_username
        hint_text: "Enter username"
        helper_text_mode: "on_error"
        icon_right: "account-box"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        size_hint_x: None
        width: 300

    MDTextField:
        id: login_password
        hint_text: "Enter password"
        password: True
        helper_text_mode: "on_error"
        icon_right: "lock"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        size_hint_x: None
        width: 300

    MDFillRoundFlatButton:
        text: "Log in"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: app.login(root.ids.login_username.text, root.ids.login_password.text)

    MDFillRoundFlatButton:
        text: "Create an account"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.manager.current = 'Register'

<RegisterScreen>:
    name: 'Register'
    MDLabel:
        text: "Create a new account"
        theme_text_color: "Primary"
        halign: "center"
        font_style: "H6"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    MDTextField:
        id: username
        hint_text: "Create an username"
        helper_text_mode: "on_error"
        icon_right: "account-box"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        size_hint_x: None
        width:300

    MDTextField:
        id: password
        hint_text: "Create a password"
        icon_right: "lock"
        password: True
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        size_hint_x: None
        width:300

    MDTextField:
        id: first_name
        hint_text: "First Name"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint_x: None
        width:300

    MDTextField:
        id: last_name
        hint_text: "Last Name"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        size_hint_x: None
        width:300

    MDFillRoundFlatButton:
        text: "Create an account"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_release: app.create_account(root.ids.username.text, root.ids.password.text, root.ids.first_name.text, root.ids.last_name.text)

    MDIconButton:
        icon: "arrow-left-circle"
        size_hint: None, None
        size: dp(150), dp(150) 
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        elevation_normal: 12
        on_release: app.back_to_login()

<WelcomeScreen>:
    name: 'Welcome'
    MDLabel:
        text: "Welcome to BabyLingo!"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        font_style: "H5"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    MDTextField:
        id: baby_name
        hint_text: "Baby Name"
        helper_text_mode: "on_error"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.75}
        size_hint_x: None
        width:300
        mode: "rectangle"

    MDTextField:
        id: date_of_birth
        hint_text: "Date of birth"
        icon_right: "calendar-today"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.65}
        size_hint_x: None
        width: 300
        mode: "rectangle"
        on_focus: if self.focus: app.show_date_picker(1)
        readonly: True

    MDTextField:
        id: hour_of_birth
        hint_text: "Hour of birth"
        icon_right: "clock"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.55}
        size_hint_x: None
        width: 300
        mode: "rectangle"
        on_focus: if self.focus: app.show_time_picker()
        readonly: True

    MDTextField:
        id: birth_weight
        hint_text: "Weight at birth (kg)"
        icon_right: "baby-carriage"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.45}
        size_hint_x: None
        width: 300
        input_type: 'number'
        mode: "rectangle"

    MDTextField:
        id: birth_height
        hint_text: "Height at birth (cm)"
        icon_right: "human-male-height"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.35}
        size_hint_x: None
        width: 300
        input_type: 'number'
        mode: "rectangle"

    MDFloatingActionButton:
        icon: 'check-bold'
        elevation_normal: 12
        md_bg_color: 0.9, 0.68, 0.86, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_release: root.save_baby_details(root.ids.baby_name.text, root.ids.date_of_birth.text, root.ids.hour_of_birth.text, root.ids.birth_weight.text, root.ids.birth_height.text)

    MDFillRoundFlatButton:
        text: "Skip for now"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'Home'

    MDIconButton:
        icon: "arrow-right-circle"
        size_hint: None, None
        size: dp(150), dp(150) 
        pos_hint: {'center_x': 0.8, 'center_y': 0.1}
        on_press: root.manager.current = 'Home'
        elevation_normal: 12

<AddNewBabyScreen>:
    name: 'AddNewBaby'
    MDLabel:
        text: "Add new baby"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        font_style: "H5"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    MDTextField:
        id: baby_name
        hint_text: "Baby Name"
        helper_text_mode: "on_error"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.75}
        size_hint_x: None
        width:300
        mode: "rectangle"

    MDTextField:
        id: date_of_birth
        hint_text: "Date of birth"
        icon_right: "calendar-today"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.65}
        size_hint_x: None
        width: 300
        mode: "rectangle"
        on_focus: if self.focus: app.show_date_picker(5)
        readonly: True

    MDTextField:
        id: hour_of_birth
        hint_text: "Hour of birth"
        icon_right: "clock"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.55}
        size_hint_x: None
        width: 300
        mode: "rectangle"
        on_focus: if self.focus: app.show_time_picker_add_baby()
        readonly: True

    MDTextField:
        id: birth_weight
        hint_text: "Weight at birth (kg)"
        icon_right: "baby-carriage"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.45}
        size_hint_x: None
        width: 300
        input_type: 'number'
        mode: "rectangle"

    MDTextField:
        id: birth_height
        hint_text: "Height at birth (cm)"
        icon_right: "human-male-height"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.35}
        size_hint_x: None
        width: 300
        input_type: 'number'
        mode: "rectangle"

    MDFloatingActionButton:
        icon: 'check-bold'
        elevation_normal: 12
        md_bg_color: 0.9, 0.68, 0.86, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_release: root.save_baby_details(root.ids.baby_name.text, root.ids.date_of_birth.text, root.ids.hour_of_birth.text, root.ids.birth_weight.text, root.ids.birth_height.text)

    MDIconButton:
        icon: "arrow-left-circle"
        size_hint: None, None
        size: dp(150), dp(150) 
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'ChooseBaby'
        elevation_normal: 12

<ChooseBabyScreen>:
    name: 'ChooseBaby'

    BoxLayout:
        orientation: 'vertical'

        ScrollView:
            size_hint_y: 0.8
            MDList:
                id: babies_list

    MDFloatingActionButton:
        icon: "plus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        md_bg_color: 0.9, 0.68, 0.86, 1
        on_press: root.manager.current = 'AddNewBaby'

    MDIconButton:
        icon: "arrow-left-circle"
        size_hint: None, None
        size: dp(150), dp(150) 
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'Account'
        elevation_normal: 12

<UpdateBabyScreen>:
    name: 'UpdateBaby'

    MDLabel:
        text: "Update Baby"
        theme_text_color: "Custom"
        text_color: 0.9, 0.68, 0.86, 1
        halign: "center"
        font_style: "H6"
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}

    MDTextField:
        id: baby_name
        hint_text: "Baby Name"
        helper_text_mode: "on_error"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.4, 'center_y':0.75}
        size_hint_x: None
        width:300
        mode: "rectangle"

    MDFloatingActionButton:
        icon: 'check-bold'
        elevation_normal: 12
        md_bg_color: 0.9, 0.68, 0.86, 1
        pos_hint: {'center_x': 0.80, 'center_y': 0.75}
        on_press: root.update_baby_name(root.ids.baby_name.text)

    MDTextField:
        id: date_of_birth
        hint_text: "Date of birth"
        icon_right: "calendar-today"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.4, 'center_y':0.65}
        size_hint_x: None
        width: 300
        mode: "rectangle"
        on_focus: if self.focus: app.show_date_picker(4)
        readonly: True

    MDFloatingActionButton:
        icon: 'check-bold'
        elevation_normal: 12
        md_bg_color: 0.9, 0.68, 0.86, 1
        pos_hint: {'center_x': 0.80, 'center_y': 0.65}
        on_press: root.update_date_of_birth(root.ids.date_of_birth.text)

    MDTextField:
        id: hour_of_birth
        hint_text: "Hour of birth"
        icon_right: "clock"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.4, 'center_y':0.55}
        size_hint_x: None
        width: 300
        mode: "rectangle"
        on_focus: if self.focus: app.show_time_picker_for_update_baby()
        readonly: True

    MDFloatingActionButton:
        icon: 'check-bold'
        elevation_normal: 12
        md_bg_color: 0.9, 0.68, 0.86, 1
        pos_hint: {'center_x': 0.80, 'center_y': 0.55}
        on_press: root.update_hour_of_birth(root.ids.hour_of_birth.text)

    MDTextField:
        id: birth_weight
        hint_text: "Weight at birth (kg)"
        icon_right: "baby-carriage"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.4, 'center_y':0.45}
        size_hint_x: None
        width: 300
        input_type: 'number'
        mode: "rectangle"

    MDFloatingActionButton:
        icon: 'check-bold'
        elevation_normal: 12
        md_bg_color: 0.9, 0.68, 0.86, 1
        pos_hint: {'center_x': 0.80, 'center_y': 0.45}
        on_press: root.update_birth_weight(root.ids.birth_weight.text)

    MDTextField:
        id: birth_height
        hint_text: "Height at birth (cm)"
        icon_right: "human-male-height"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.4, 'center_y':0.35}
        size_hint_x: None
        width: 300
        input_type: 'number'
        mode: "rectangle"

    MDFloatingActionButton:
        icon: 'check-bold'
        elevation_normal: 12
        md_bg_color: 0.9, 0.68, 0.86, 1
        pos_hint: {'center_x': 0.80, 'center_y': 0.35}
        on_press: root.update_birth_height(root.ids.birth_height.text)

    MDIconButton:
        icon: "arrow-left-circle"
        size_hint: None, None
        size: dp(150), dp(150) 
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'ChooseBaby'
        elevation_normal: 12

<HomeScreen>:        
    name: 'Home'
    MDLabel:
        text: "Record your baby"
        theme_text_color: "Custom"
        text_color: 0.9, 0.68, 0.86, 1
        halign: "center"
        font_style: "H6"
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}

    MDIconButton:
        icon: "account-details"
        size_hint: None, None
        size: dp(150), dp(150) 
        pos_hint: {'center_x': 0.1, 'center_y': 0.95}
        on_press: root.manager.current = 'Account'
        elevation_normal: 12

    MDFloatingActionButton:
        icon: 'microphone'
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}  
        md_bg_color: 0.9, 0.68, 0.86, 1
        on_press: root.start_recording()
        size: dp(200), dp(200)  
        elevation_normal: 12

    MDRaisedButton:
        text: "Stop Recording"
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}  
        on_press: root.stop_recording()
        size_hint: None, None
        size: dp(200), dp(60)  
        font_size: '18sp' 


    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            id: notification_bar
            size_hint_y: None
            height: 0
            pos_hint: {'top': 1}
            canvas.before:
                Color:
                    rgba: 1, 0, 0, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

            Label:
                text: ""
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_y: None
                height: self.texture_size[1]
                color: [1, 1, 1, 1]

<AccountScreen>:
    name: 'Account'
    MDLabel:
        text: "Manage your Account"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0.9, 0.68, 0.86, 1
        font_style: "H6"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    MDTextField:
        id: password
        hint_text: "Update password"
        helper_text_mode: "on_error"
        pos_hint: {'center_x': 0.35, 'center_y': 0.7}
        size_hint_x: None
        width: 250

    MDFloatingActionButton:
        icon: 'check-bold'
        elevation_normal: 12
        md_bg_color: 0.9, 0.68, 0.86, 1
        pos_hint: {'center_x': 0.75, 'center_y': 0.7}
        on_press: root.update_password()

    MDTextField:
        id: first_name
        hint_text: "Update first name"
        helper_text_mode: "on_error"
        pos_hint: {'center_x': 0.35, 'center_y': 0.6}
        size_hint_x: None
        width: 250

    MDFloatingActionButton:
        icon: 'check-bold'
        elevation_normal: 12
        md_bg_color: 0.9, 0.68, 0.86, 1
        pos_hint: {'center_x': 0.75, 'center_y': 0.6}
        on_press: root.update_first_name()

    MDTextField:
        id: last_name
        hint_text: "Update last name"
        helper_text_mode: "on_error"
        pos_hint: {'center_x': 0.35, 'center_y': 0.5}
        size_hint_x: None
        width: 250

    MDFloatingActionButton:
        icon: 'check-bold'
        elevation_normal: 12
        md_bg_color: 0.9, 0.68, 0.86, 1
        pos_hint: {'center_x': 0.75, 'center_y': 0.5}
        on_press: root.update_last_name()

    MDFillRoundFlatButton:
        text: "Update baby info"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: root.manager.current = 'ChooseBaby'

    MDFillRoundFlatButton:
        text: "Logout"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.manager.current = 'Login'

    MDRaisedButton:
        text: "Delete your account"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        md_bg_color: 0.9, 0.68, 0.86, 1
        on_press: root.show_delete_confirmation()

    MDIconButton:
        icon: "arrow-right-circle"
        size_hint: None, None
        size: dp(150), dp(150) 
        pos_hint: {'center_x': 0.8, 'center_y': 0.1}
        on_press: root.manager.current = 'Home'
        elevation_normal:2

"""