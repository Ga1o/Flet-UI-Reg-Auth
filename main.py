import flet as ft
from db_conn import User, session


def main(page: ft.Page):
    page.title = 'Base reg auth app'
    page.window_width = 380
    page.window_height = 650
    page.theme_mode = 'dark'
    page.window_resizable = False

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    def register(e):
        user = session.query(User).filter_by(user_email=user_email.value).first()
        if not user:
            user = User(user_name=user_name.value, user_email=user_email.value, user_password=password.value)
            session.add(user)
            session.commit()

        user_name.value = ''
        user_email.value = ''
        password.value = ''
        page.update()

    def login_link(e):
        page.remove(reg_panel)
        page.add(auth_panel)
        page.update()

    def register_link(e):
        page.remove(auth_panel)
        page.add(reg_panel)
        page.update()

    def login(e):
        user = session.query(User).filter_by(user_email=user_email.value, user_password=password.value).first()
        if not user:
            page.snack_bar = ft.SnackBar(ft.Text('Wrong data'))
            page.snack_bar.open = True
            page.update()

        else:
            page.snack_bar = ft.SnackBar(ft.Text('Auth success'))
            page.snack_bar.open = True
            page.clean()
            page.add(top_panel)
            page.add(dashboard_panel)
            page.update()

    def reg_validate(e):
        if all([user_email.value, password.value]):
            sub_reg.disabled = False
            sub_auth.disabled = False
        else:
            sub_reg.disabled = True
            sub_auth.disabled = True

        page.update()

    def user_setts(e):
        page.remove(dashboard_panel)
        page.add(ft.Text())
        page.add(settings_panel)
        page.update()

    def logout(e):
        page.remove(settings_panel)
        page.add(auth_panel)
        page.update()

    top_text = ft.Text(value='BASE APP', text_align=ft.TextAlign.CENTER)

    user_name = ft.TextField(label='Name', on_change=reg_validate)
    user_email = ft.TextField(label='Email', on_change=reg_validate)
    password = ft.TextField(label='Password', password=True, on_change=reg_validate)

    sub_reg = ft.OutlinedButton(text='Register', width=page.window_width, height=50, on_click=register, disabled=True)
    sub_auth = ft.OutlinedButton(text='Login', width=page.window_width, height=50, on_click=login, disabled=True)
    logout_btn = ft.OutlinedButton(text='Logout', width=page.window_width, height=50, on_click=logout)

    to_login_btn = ft.OutlinedButton(text='Login', width=page.window_width, height=50, on_click=login_link)
    to_reg_btn = ft.OutlinedButton(text='Register', width=page.window_width, height=50, on_click=register_link)

    user_settings = ft.OutlinedButton(text='Settings', width=page.window_width, height=50, on_click=user_setts)

    top_panel = ft.Row(
            [
                top_text,
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

    reg_panel = ft.Column(
            [
                ft.Text('Register'),
                user_name,
                user_email,
                password,
                sub_reg,
                to_login_btn,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            height=400,
        )

    auth_panel = ft.Column(
        [
            ft.Text('Login'),
            user_email,
            password,
            sub_auth,
            to_reg_btn,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        height=400,
    )

    dashboard_panel = ft.Column(
        [
            ft.Text('Dashboard'),
            user_settings,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        height=400,
    )

    settings_panel = ft.Column(
        [
            ft.Text('Settings'),
            logout_btn,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        height=400,
    )

    page.add(top_panel)
    page.add(auth_panel)


ft.app(main)

