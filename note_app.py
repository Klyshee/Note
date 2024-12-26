import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение для заметок")
        self.notes = self.load_notes()

        self.note_listbox = tk.Listbox(root, width=50, height=15)
        self.note_listbox.pack(pady=10)

        tk.Button(root, text="Добавить заметку", command=self.add_note).pack(pady=5)
        tk.Button(root, text="Редактировать заметку", command=self.edit_note).pack(pady=5)
        tk.Button(root, text="Удалить заметку", command=self.delete_note).pack(pady=5)
        tk.Button(root, text="Сохранить заметки", command=self.save_notes).pack(pady=5)

        self.search_entry = tk.Entry(root)
        self.search_entry.pack(pady=5)
        self.search_entry.bind("<KeyRelease>", self.search_notes)

        self.update_listbox()

    def add_note(self):
        note = simpledialog.askstring("Добавить заметку", "Введите текст заметки:")
        if note:
            self.notes.append(note)
            self.update_listbox()

    def edit_note(self):
        idx = self.note_listbox.curselection()
        if idx:
            note = simpledialog.askstring("Редактировать заметку", "Введите новый текст заметки:", initialvalue=self.notes[idx[0]])
            if note:
                self.notes[idx[0]] = note
                self.update_listbox()
        else:
            messagebox.showwarning("Редактировать заметку", "Сначала выберите заметку.")

    def delete_note(self):
        idx = self.note_listbox.curselection()
        if idx:
            del self.notes[idx[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Удалить заметку", "Сначала выберите заметку.")

    def save_notes(self):
        with open("notes.json", "w") as f:
            json.dump(self.notes, f)
        messagebox.showinfo("Сохранение заметок", "Заметки успешно сохранены!")

    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as f:
                return json.load(f)
        return []

    def update_listbox(self):
        self.note_listbox.delete(0, tk.END)
        for note in self.notes:
            self.note_listbox.insert(tk.END, note)

    def search_notes(self, event):
        search_term = self.search_entry.get().lower()
        self.note_listbox.delete(0, tk.END)
        for note in self.notes:
            if search_term in note.lower():
                self.note_listbox.insert(tk.END, note)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
