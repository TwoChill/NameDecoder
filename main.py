# IMPORTS
import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout  # Import BoxLayout
from kivy.animation import Animation
from kivy.core.video import Video
from kivy.uix.videoplayer import VideoPlayer

# Install ffpyplayer to play videos.

# VARIABLES
os.environ["KIVY_VIDEO"] = "ffpyplayer"
LOGO = '3.png'


class NameDecoder(App):
    """
    A Kivy application for numerology name analysis.
    """

    def build(self):
        """
        Build the main application window.

        Returns:
            GridLayout: The root layout of the application.
        """
        self.window = GridLayout()
        self.window.cols = 1

        # Image size margin (sides, top and bottom)
        self.window.size_hint = (0.60, 0.70)
        # Image position (horizontally, vertically)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        return self.window

    def on_start(self):
        """
        Initialize and animate the application elements when it starts.

        This function sets up the logo animation and initializes input box and
        convert button, making them visible with a fade-in animation.
        """
        # Logo widget with initial opacity of 0
        self.logo = Image(source=LOGO, allow_stretch=False, opacity=0)
        self.window.add_widget(self.logo)

        # Sequential animation: Fade in the logo, then input box and button
        fade_in_logo = Animation(opacity=1, duration=3)
        fade_in_input_button = Animation(opacity=1, duration=3)

        # Define a callback function for the end of the fade-in logo animation
        def on_logo_fade_in_finish(animation, widget):
            # After the logo fades in, start the fade-in animation for input box and button
            fade_in_input_button.start(self.input_box)
            fade_in_input_button.start(self.convert_button)

        # Bind the callback function to the end of the fade-in logo animation
        fade_in_logo.bind(on_complete=on_logo_fade_in_finish)

        # Input box and convert button with initial opacity of 0
        self.input_box = TextInput(multiline=False,
                                   hint_text='Enter your name',
                                   padding=(10, 20),
                                   size_hint=(1, 0.20),
                                   opacity=0
                                   )

        self.convert_button = Button(text='Convert',
                                     size_hint=(1, 0.20),
                                     bold=True,
                                     background_color=("#FC3030"),
                                     background_normal='',
                                     opacity=0
                                     )

        # Bind the on_release event of the button to the convert_name method
        self.convert_button.bind(on_release=self.convert_name)

        # Add the input box and convert button to the window (initially invisible)
        self.window.add_widget(self.input_box)
        self.window.add_widget(self.convert_button)

        # Start the fade-in logo animation
        fade_in_logo.start(self.logo)

    def convert_name(self, _):
        """
        Convert the entered name to a numerology number and play the associated video.

        Args:
            _: Unused argument.
        """
        # Remove all widgets from the window
        self.window.clear_widgets()

        # Create a layout to hold the video player
        video_layout = BoxLayout(orientation='vertical')

        # Create and add the video player to the layout
        video_filename = f"{self.calculate_number(self.input_box.text)}.mp4"
        video_path = os.path.join(os.path.dirname(__file__), video_filename)
        if os.path.exists(video_path):
            video_player = VideoPlayer(source=video_path, state='play')
            video_layout.add_widget(video_player)  # Add the VideoPlayer to the layout
            self.window.add_widget(video_layout)  # Add the layout to the window
        else:
            # Use a placeholder video with a message
            not_found_video_path = os.path.join(os.path.dirname(__file__), "not_found.mp4")
            if os.path.exists(not_found_video_path):
                video_player = VideoPlayer(source=not_found_video_path, state='play')
                video_layout.add_widget(video_player)
            else:
                # Display a message if the placeholder video is also not found
                label = Label(text=f"Video '{video_filename}' not found.")
                video_layout.add_widget(label)
                self.window.add_widget(video_layout)  # Add the layout to the window
                print(f"Video '{video_filename}' not found.")

    def calculate_number(self, name):
        """
        Calculate the numerology number for a given name.

        Args:
            name (str): The name to be converted.

        Returns:
            str: The numerology number calculated from the name.
        """
        name = name.upper()  # Convert the name to uppercase for consistency
        number_mapping = {
            '1': ['A', 'J', 'S'],
            '2': ['B', 'K', 'T'],
            '3': ['C', 'L', 'U'],
            '4': ['D', 'M', 'V'],
            '5': ['E', 'N', 'W'],
            '6': ['F', 'O', 'X'],
            '7': ['G', 'P', 'Y'],
            '8': ['H', 'Q', 'Z'],
            '9': ['I', 'R']
        }

        special_numbers = ['11', '22', '33']  # Master Numbers

        total = 0

        for letter in name:
            for number, letters in number_mapping.items():
                if letter in letters:
                    total += int(number)
                    break  # Move to the next letter

        while str(total) not in special_numbers and total > 9:
            total = sum(int(digit) for digit in str(total))

        return str(total)

    def play_video(self, number):
        video_filename = f"{number}.mp4"
        video_path = os.path.join(os.path.dirname(__file__), video_filename)

        if os.path.exists(video_path):
            video = Video(source=video_path, state='play')
            self.window.clear_widgets()  # Clear existing widgets
            self.window.add_widget(video)  # Add the video to the layout
        else:
            print(f"Video '{video_filename}' not found.")


if __name__ == '__main__':
    NameDecoder().run()
