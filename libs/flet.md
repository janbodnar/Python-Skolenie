# Flet

The Flet Python library is a framework that allows developers to build interactive web,  
desktop, and mobile applications using Python, without requiring prior experience in  
frontend development. Flet is built on top of Flutter, a UI toolkit by Google, and provides  
a set of controls and widgets to create polished and professional-looking applications.

Key Features:

- Multi-Platform Support: Build applications for web, desktop (Windows, macOS, Linux),
  and mobile (iOS, Android).  
- User-Friendly: Simplifies frontend development by combining smaller widgets into
  ready-to-use controls.  
- No Frontend Experience Needed: You don't need to know HTML, CSS, or JavaScript to  
  create UI with Flet.  
- Stylish UI: Ensures your applications look modern and polished without additional
- design efforts.

## Center

```python
import flet as ft

def main(page: ft.Page):
  
#   page.window_title_bar_hidden = True
  page.title = 'Centered window'
  page.window_center()

ft.app(target=main)
```

## text control

```python
import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

ft.app(target=main)
```

## Button click

```python
import flet as ft

def main(page: ft.Page):
  
  def on_click_btn(_: ft.ControlEvent):
    page.window_close()

  btn = ft.ElevatedButton(
      text="Click Me",
      on_click=on_click_btn,
  )


  page.add(btn)

ft.app(target=main)
```

```python
import flet
from flet import Page, ElevatedButton


def main(page: Page):
    def on_click_btn(e):
        print("i was clicked!")

    def on_hover_btn(e):
        print("why you hovering on me!")

    def on_longpress_btn(e):
        print("you pressed me so long!")

    btn = ElevatedButton(
        text="Click Me",
        on_click=on_click_btn,
        on_hover=on_hover_btn,
        on_long_press=on_longpress_btn
    )

    page.window_resizable = False
    page.add(btn)


a = flet.app(target=main)
# page.window_width = 200
# page.window_height = 200
print(a)
```

## Navbar

```python
import flet as ft


def main(page: ft.Page):
    def addNavBar():
#adding navigation bar to page when this function is called
        page.navigation_bar = ft.NavigationBar(
        destinations=[
#icon 1 , with Flet built-in icon image and Label
            ft.NavigationDestination(icon=ft.icons.HOME_ROUNDED ,label="Home", ),
#icon 1 , with Flet built-in icon image and Label           
            ft.NavigationDestination(
                icon=ft.icons.SETTINGS_ROUNDED,
                label="Settings",
            ),
            
        ]
        ,bgcolor="Blue"
    )
    page.window_width=600
    page.window_height=850
    page.bgcolor="#DFF6FF"
    page.title="World Bank App"

#add navigation bar   
    addNavBar()
    page.update()
    
ft.app(target=main, view=ft.WEB_BROWSER)
```

## Checkbox

```python
import flet as ft


def main(page: ft.Page):

    def on_changed(e: ft.ControlEvent):

        print(e.data)

        if e.data == 'true':
            page.title = 'Application'
        else:
            page.title = ' '
        page.update()

    c1 = ft.Checkbox(label="Show title", value=True, on_change=on_changed)
    
    page.window_width = 200
    page.window_height = 200
    page.title = 'Application'

    page.add(c1)
    page.update()

ft.app(target=main)

# def button_clicked(e):
#     t.value = (
#         f"Checkboxes values are:  {c1.value}, {
#             c2.value}, {c3.value}, {c4.value}, {c5.value}."
#     )
#     page.update()

# c2 = ft.Checkbox(
#     label="Undefined by default tristate checkbox", tristate=True)
# c3 = ft.Checkbox(label="Checked by default checkbox", value=True)
# c4 = ft.Checkbox(label="Disabled checkbox", disabled=True)
# c5 = ft.Checkbox(
#     label="Checkbox with rendered label_position='left'", label_position=ft.LabelPosition.LEFT
# )

# b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
# page.add(c1, c2, c3, c4, c5, b, t)
```


## Custom control

```python

import flet as ft


class MyControl(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()

        self._row = ft.Row(spacing=30, scroll=ft.ScrollMode.AUTO,
                           alignment=ft.MainAxisAlignment.CENTER)
        num_fields = 4
        page.window_width = 150 * num_fields
        self._row.controls = [ft.TextField(
            label="Some Field") for _ in range(num_fields)]
        page.update()

    def build(self):
        return self._row


def main(page: ft.Page):
    page.padding = 25
    theme = ft.Theme()
    theme.visual_density = ft.ThemeVisualDensity.COMPACT
    page.theme = theme
    page.theme_mode = ft.ThemeMode.LIGHT

    my_control = MyControl(page)

    page.add(
        my_control
    )


ft.app(target=main)
```

## Canvas

```python
import math
import flet as ft
import flet.canvas as cv

def main(page: ft.Page):

    stroke_paint = paint = ft.Paint(color=ft.colors.GREEN_500, stroke_width=2, style=ft.PaintingStyle.STROKE)
    fill_paint = paint = ft.Paint(color=ft.colors.GREEN_500, style=ft.PaintingStyle.FILL)
    cp = cv.Canvas(
        [
            cv.Circle(100, 100, 50, stroke_paint),
            cv.Circle(80, 90, 10, stroke_paint),
            cv.Circle(84, 87, 5, fill_paint),
            cv.Circle(120, 90, 10, stroke_paint),
            cv.Circle(124, 87, 5, fill_paint),
            cv.Arc(70, 95, 60, 40, 0, math.pi, paint=stroke_paint),
        ],
        width=float("inf"),
        expand=True,
    )

    page.add(cp)

ft.app(main)
```

