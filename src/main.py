"""
Author: Brian Turza
Created: 22th May 2021
"""
class Tabsterr:
    def __init__(self):
        self.audio = ""
        self.output = ""
    def transcribe(self, tabs):
        self.ascii_format(tabs)
        return self.output

    def ascii_format(self, tabs):
        self.output = f"""
       | {"-" * (len(max(tabs)) + len(max(tabs)) - 1)} |
    E  | {"-".join([i.replace('', '-') for i in tabs[0]])} |
    A  | {"-".join([i for i in tabs[1]])} |
    D  | {"-".join([i for i in tabs[2]])} | 
    G  | {"-".join([i for i in tabs[3]])} |
    B  | {"-".join([i for i in tabs[4]])} |
    E  | {"-".join([i for i in tabs[5]])} | 
    """

if __name__ == "__main__":
    arr = [
        ["0", "0", "0", "0"],
        ["", "", "", "", "2"],
        ["", "", "", "", "4"],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""]
    ]
    t = Tabsterr()
    print(t.transcribe(arr))
    # n + (n - 1)
    #