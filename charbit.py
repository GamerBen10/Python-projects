from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

# Set mobile-friendly preview window size for desktop testing
Window.size = (380, 680)
Window.clearcolor = (0.07, 0.07, 0.11, 1.0)  # Dark background


class MessageBubble(BoxLayout):
    """Chat bubble widget formatted for sender type."""
    def __init__(self, sender, text, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.padding = [dp(10), dp(6)]
        self.spacing = dp(2)

        is_user = (sender == "You")
        sender_color = (0.65, 0.89, 0.63, 1.0) if is_user else (0.54, 0.71, 0.98, 1.0)

        # Sender Name Header
        header = Label(
            text=f"[b]{sender}[/b]",
            markup=True,
            color=sender_color,
            font_size="13sp",
            size_hint_y=None,
            height=dp(18),
            halign="left" if not is_user else "right",
        )
        header.bind(size=header.setter("text_size"))
        self.add_widget(header)

        # Message Body Text
        body = Label(
            text=text,
            color=(0.8, 0.84, 0.96, 1.0),
            font_size="14sp",
            size_hint_y=None,
            halign="left" if not is_user else "right",
        )
        body.bind(
            width=lambda instance, val: setattr(instance, "text_size", (val, None))
        )
        body.bind(
            texture_size=lambda instance, val: self._update_height(body, val[1])
        )
        self.add_widget(body)

    def _update_height(self, body_widget, text_height):
        body_widget.height = text_height
        self.height = text_height + dp(32)


class LegalChatbotAndroid(App):
    def build(self):
        root = BoxLayout(orientation="vertical")

        # 1. Top Legal Disclaimer Banner
        disclaimer = Label(
            text="⚠️ [b]Disclaimer:[/b] LexisBot provides legal info, not formal legal advice.",
            markup=True,
            size_hint_y=None,
            height=dp(36),
            font_size="11sp",
            color=(0.95, 0.55, 0.66, 1.0),
        )
        root.add_widget(disclaimer)

        # 2. Quick Practice Area Horizontal Scroll Selector
        category_bar = ScrollView(size_hint_y=None, height=dp(42), do_scroll_y=False)
        cat_layout = GridLayout(rows=1, size_hint_x=None, spacing=dp(8), padding=[dp(8), dp(2)])
        cat_layout.bind(minimum_width=cat_layout.setter("width"))

        practice_areas = [
            "Contracts",
            "Employment",
            "Intellectual Property",
            "Compliance",
            "Tenancy Law",
            "Reset Chat",
        ]

        for area in practice_areas:
            btn = Button(
                text=area,
                size_hint=(None, None),
                size=(dp(120), dp(34)),
                font_size="12sp",
                background_normal="",
                background_color=(0.19, 0.20, 0.27, 1.0),
                color=(0.8, 0.84, 0.96, 1.0),
            )
            btn.bind(on_press=self._on_category_click)
            cat_layout.add_widget(btn)

        category_bar.add_widget(cat_layout)
        root.add_widget(category_bar)

        # 3. Main Chat History (Vertical Scroll)
        self.chat_scroll = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        self.chat_layout = GridLayout(
            cols=1,
            size_hint_y=None,
            spacing=dp(10),
            padding=[dp(10), dp(10)],
        )
        self.chat_layout.bind(minimum_height=self.chat_layout.setter("height"))
        self.chat_scroll.add_widget(self.chat_layout)
        root.add_widget(self.chat_scroll)

        # 4. Bottom Input Bar (TextInput + Send Button)
        input_bar = BoxLayout(
            size_hint_y=None,
            height=dp(52),
            padding=[dp(8), dp(6)],
            spacing=dp(8),
        )

        self.input_field = TextInput(
            hint_text="Ask a legal question...",
            multiline=False,
            font_size="14sp",
            background_color=(0.12, 0.12, 0.18, 1.0),
            foreground_color=(0.8, 0.84, 0.96, 1.0),
            hint_text_color=(0.5, 0.5, 0.6, 1.0),
            cursor_color=(0.54, 0.71, 0.98, 1.0),
            padding=[dp(10), dp(10)],
        )
        self.input_field.bind(on_text_validate=self._send_message)
        input_bar.add_widget(self.input_field)

        send_btn = Button(
            text="Send",
            size_hint=(None, 1),
            width=dp(70),
            font_size="13sp",
            bold=True,
            background_normal="",
            background_color=(0.54, 0.71, 0.98, 1.0),
            color=(0.07, 0.07, 0.11, 1.0),
        )
        send_btn.bind(on_press=self._send_message)
        input_bar.add_widget(send_btn)

        root.add_widget(input_bar)

        # Initial Welcome Bubble
        Clock.schedule_once(
            lambda dt: self._add_bubble(
                "LexisBot",
                "Welcome. Tap a practice area above or type your legal question to get started.",
            ),
            0.1,
        )

        return root

    def _add_bubble(self, sender, text):
        bubble = MessageBubble(sender=sender, text=text)
        self.chat_layout.add_widget(bubble)
        # Scroll to bottom
        Clock.schedule_once(lambda dt: setattr(self.chat_scroll, "scroll_y", 0), 0.1)

    def _send_message(self, *args):
        user_text = self.input_field.text.strip()
        if not user_text:
            return

        self._add_bubble("You", user_text)
        self.input_field.text = ""

        # UI Placeholder simulating asynchronous response
        Clock.schedule_once(
            lambda dt: self._add_bubble(
                "LexisBot", "[Android backend response logic pending connection...]"
            ),
            0.5,
        )

    def _on_category_click(self, instance):
        category = instance.text
        if category == "Reset Chat":
            self.chat_layout.clear_widgets()
            self._add_bubble("LexisBot", "Chat history cleared. Enter a new query.")
        else:
            self._add_bubble(
                "LexisBot",
                f"Practice area switched to **{category}**. What specific legal questions or clauses do you need examined?",
            )


if __name__ == "__main__":
    LegalChatbotAndroid().run()
