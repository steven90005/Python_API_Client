import tkinter as tk
import requests

class APIClient:
    def __init__(self, root):
        self.root = root
        self.root.title("API Client")

        # API URL 輸入
        tk.Label(self.root, text="API URL:").grid(row=0, column=0)
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.grid(row=0, column=1)

        # HTTP method 
        tk.Label(self.root, text="HTTP Method:").grid(row=1, column=0)
        self.method_var = tk.StringVar()
        self.method_var.set("GET")
        tk.OptionMenu(self.root, self.method_var, "POST", "GET", "DELETE").grid(row=1, column=1)

        # Content type 
        tk.Label(self.root, text="Content Type:").grid(row=2, column=0)
        self.content_type_var = tk.StringVar()
        self.content_type_var.set("application/json")
        tk.OptionMenu(self.root, self.content_type_var, "application/json", "application/xml", "text/plain").grid(row=2, column=1)

        # 發送訊息
        tk.Label(self.root, text="發送訊息:").grid(row=3, column=0)
        self.body_text = tk.Text(self.root, height=10, width=50)
        self.body_text.grid(row=3, column=1)

        # 回覆視窗
        tk.Label(self.root, text="回覆視窗:").grid(row=4, column=0)
        self.response_text = tk.Text(self.root, height=10, width=50)
        self.response_text.grid(row=4, column=1)

        # 發送按鈕
        tk.Button(self.root, text="發送", command=self.send_request).grid(row=5, column=1)

    def send_request(self):
        url = self.url_entry.get()
        method = self.method_var.get()
        content_type = self.content_type_var.get()
        body = self.body_text.get("1.0", tk.END).strip()

        headers = {"Content-Type": content_type}

        try:
            response = None
            if method == "POST":
                response = requests.post(url, headers=headers, data=body)
            elif method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)

            if response is not None:
                self.response_text.delete("1.0", tk.END)
                self.response_text.insert(tk.END, response.text)
        except requests.exceptions.RequestException as e:
            self.response_text.delete("1.0", tk.END)
            self.response_text.insert(tk.END, str(e))

if __name__ == "__main__":
    root = tk.Tk()
    APIClient(root)
    root.mainloop()
