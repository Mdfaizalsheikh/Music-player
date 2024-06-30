import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")
        
        pygame.init()
        pygame.mixer.init()
        
        self.track_list = []
        self.current_track_index = 0
        
        self.track_label = tk.Label(root, text="No track loaded", font=("Helvetica", 12))
        self.track_label.pack(pady=10)
        
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(side="left", padx=10, pady=10)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(side="left", padx=10, pady=10)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side="left", padx=10, pady=10)
        
        self.prev_button = tk.Button(root, text="Previous", command=self.prev_track)
        self.prev_button.pack(side="left", padx=10, pady=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_track)
        self.next_button.pack(side="left", padx=10, pady=10)
        
        self.load_button = tk.Button(root, text="Load Tracks", command=self.load_tracks)
        self.load_button.pack(pady=10)

    def load_tracks(self):
        directory = filedialog.askdirectory()
        if directory:
            self.track_list = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".mp3")]
            if self.track_list:
                self.current_track_index = 0
                self.load_track()

    def load_track(self):
        track_path = self.track_list[self.current_track_index]
        self.track_label.config(text=os.path.basename(track_path))
        pygame.mixer.music.load(track_path)

    def play_music(self):
        pygame.mixer.music.play()
        
    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    
    def stop_music(self):
        pygame.mixer.music.stop()

    def prev_track(self):
        if self.current_track_index > 0:
            self.current_track_index -= 1
            self.load_track()
            self.play_music()

    def next_track(self):
        if self.current_track_index < len(self.track_list) - 1:
            self.current_track_index += 1
            self.load_track()
            self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
