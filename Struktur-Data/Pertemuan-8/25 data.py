from collections import deque
import time
class Mytree:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def showTree(self, level=0):
        print("  "*level + f"->{self.name}")
        for child in self.children:
            child.showTree(level+1)

    def Dfs_search(self, target):
        if self.name == target:
            return self
        for child in self.children:
            result = child.Dfs_search(target)
            if result:
                return result
        return None
    
    def Bfs_search(self, target):
        queue = deque([self])
        while queue:
            current = queue.popleft()
            if current.name == target:
                return current
            queue.extend(current.children)
        return None

# Buat node utama
root = Mytree("Menu Utama")
account = Mytree("Account")
setting = Mytree("Setting")
profile = Mytree("Profile")
security = Mytree("Security")
display = Mytree("Display")
notif = Mytree("Notification")
dashboard = Mytree("Dashboard")
tambah = Mytree("Tambah data")

# Tambahan node lainnya
help_menu = Mytree("Help")
logout = Mytree("Logout")
about = Mytree("About")
faq = Mytree("FAQ")
themes = Mytree("Themes")
brightness = Mytree("Brightness")
privacy = Mytree("Privacy")
language = Mytree("Language")
feedback = Mytree("Feedback")
report_bug = Mytree("Report Bug")
activity_log = Mytree("Activity Log")
invite_friends = Mytree("Invite Friends")
data_export = Mytree("Data Export")
data_import = Mytree("Data Import")
analytics = Mytree("Analytics")
log = Mytree("Log")

# Bangun struktur pohon
root.addChild(account)
root.addChild(setting)
root.addChild(dashboard)
root.addChild(help_menu)
root.addChild(logout)

account.addChild(profile)
account.addChild(security)
account.addChild(privacy)
account.addChild(activity_log)

setting.addChild(notif)
setting.addChild(display)
setting.addChild(language)
setting.addChild(themes)
setting.addChild(brightness)

display.addChild(brightness)

dashboard.addChild(tambah)
dashboard.addChild(analytics)
dashboard.addChild(log)

help_menu.addChild(about)
help_menu.addChild(faq)
help_menu.addChild(feedback)
help_menu.addChild(report_bug)
help_menu.addChild(invite_friends)

tambah.addChild(data_export)
tambah.addChild(data_import)
print(root.showTree())

mulaicari_dfs = time.time()
pencarianDfs = root.Dfs_search("faQ")
selesaicari_dfs = time.time()
waktucari_dfs = selesaicari_dfs - mulaicari_dfs
print(f"data ditemukan via DFS: {pencarianDfs.name if pencarianDfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk DFS search adalah: {waktucari_dfs * 1000:.3f}")


mulaicari_bfs = time.time()
pencarianBfs = root.Bfs_search("faQ")
selesaicari_bfs = time.time()
waktucari_bfs = selesaicari_bfs - mulaicari_bfs
print(f"data ditemukan via BFS: {pencarianBfs.name if pencarianBfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk BFS search adalah: {waktucari_bfs * 1000:.3f}")