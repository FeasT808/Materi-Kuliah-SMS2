from collections import deque
import time
class Mytree:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def showTree(self, level=0):
        print("-"*level + f"->{self.name}")
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

# === Node Utama ===
root = Mytree("Menu Utama")
account = Mytree("Account")
setting = Mytree("Setting")
profile = Mytree("Profile")
security = Mytree("Security")
display = Mytree("Display")
notif = Mytree("Notification")
dashboard = Mytree("Dashboard")
tambah = Mytree("Tambah data")

# === Tambahan sebelumnya ===
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

notif_email = Mytree("Email Notification")
notif_sms = Mytree("SMS Notification")
notif_push = Mytree("Push Notification")
theme_dark = Mytree("Dark Mode")
theme_light = Mytree("Light Mode")
backup = Mytree("Backup")
restore = Mytree("Restore")
terms = Mytree("Terms & Conditions")
security_question = Mytree("Security Question")
change_password = Mytree("Change Password")
view_profile = Mytree("View Profile")
edit_profile = Mytree("Edit Profile")
profile_picture = Mytree("Profile Picture")
upload_avatar = Mytree("Upload Avatar")
delete_account = Mytree("Delete Account")
recent_activity = Mytree("Recent Activity")
blocked_users = Mytree("Blocked Users")
user_stats = Mytree("User Statistics")
connect_social = Mytree("Connect to Social Media")
app_version = Mytree("App Version")
system_info = Mytree("System Information")
device_settings = Mytree("Device Settings")
theme_custom = Mytree("Custom Theme")
dark_blue = Mytree("Dark Blue")
dark_red = Mytree("Dark Red")

# === Tambahan baru (total 25 node lagi) ===
support_center = Mytree("Support Center")
contact_us = Mytree("Contact Us")
live_chat = Mytree("Live Chat")
user_guide = Mytree("User Guide")
setup_tutorial = Mytree("Setup Tutorial")
keyboard_shortcuts = Mytree("Keyboard Shortcuts")
beta_features = Mytree("Beta Features")
early_access = Mytree("Early Access")
changelog = Mytree("Changelog")
download_data = Mytree("Download Data")
upload_files = Mytree("Upload Files")
file_manager = Mytree("File Manager")
storage_usage = Mytree("Storage Usage")
monthly_report = Mytree("Monthly Report")
yearly_summary = Mytree("Yearly Summary")
payment_method = Mytree("Payment Method")
billing_history = Mytree("Billing History")
invoice_download = Mytree("Invoice Download")
language_en = Mytree("English")
language_id = Mytree("Indonesian")
language_jp = Mytree("Japanese")
bug_status = Mytree("Bug Status")
feature_request = Mytree("Feature Request")
share_feedback = Mytree("Share Feedback")
system_logs = Mytree("System Logs")

# === Bangun struktur pohon ===
root.addChild(account)
root.addChild(setting)
root.addChild(dashboard)
root.addChild(help_menu)
root.addChild(logout)

account.addChild(profile)
account.addChild(security)
account.addChild(privacy)
account.addChild(activity_log)
account.addChild(delete_account)
account.addChild(blocked_users)
account.addChild(user_stats)

profile.addChild(view_profile)
profile.addChild(edit_profile)
profile.addChild(profile_picture)
profile_picture.addChild(upload_avatar)

security.addChild(security_question)
security.addChild(change_password)

setting.addChild(notif)
setting.addChild(display)
setting.addChild(language)
setting.addChild(themes)
setting.addChild(brightness)
setting.addChild(backup)
setting.addChild(restore)
setting.addChild(device_settings)

notif.addChild(notif_email)
notif.addChild(notif_sms)
notif.addChild(notif_push)

themes.addChild(theme_dark)
themes.addChild(theme_light)
themes.addChild(theme_custom)
theme_custom.addChild(dark_blue)
theme_custom.addChild(dark_red)

language.addChild(language_en)
language.addChild(language_id)
language.addChild(language_jp)

dashboard.addChild(tambah)
dashboard.addChild(analytics)
dashboard.addChild(log)
dashboard.addChild(connect_social)
dashboard.addChild(app_version)
dashboard.addChild(system_info)

tambah.addChild(data_export)
tambah.addChild(data_import)
tambah.addChild(file_manager)
file_manager.addChild(upload_files)
file_manager.addChild(download_data)
file_manager.addChild(storage_usage)

analytics.addChild(monthly_report)
analytics.addChild(yearly_summary)

setting.addChild(payment_method)
setting.addChild(billing_history)
billing_history.addChild(invoice_download)

help_menu.addChild(about)
help_menu.addChild(faq)
help_menu.addChild(feedback)
help_menu.addChild(report_bug)
help_menu.addChild(invite_friends)
help_menu.addChild(terms)
help_menu.addChild(support_center)
help_menu.addChild(contact_us)
support_center.addChild(live_chat)
support_center.addChild(user_guide)
support_center.addChild(setup_tutorial)
help_menu.addChild(keyboard_shortcuts)
help_menu.addChild(beta_features)
beta_features.addChild(early_access)
beta_features.addChild(changelog)
report_bug.addChild(bug_status)
feedback.addChild(feature_request)
feedback.addChild(share_feedback)

dashboard.addChild(system_logs)
# === Menampilkan Tree ===
print(root.showTree())

mulaicari_dfs = time.time()
pencarianDfs = root.Dfs_search("App Version")
selesaicari_dfs = time.time()
waktucari_dfs = selesaicari_dfs - mulaicari_dfs
print(f"data ditemukan via DFS: {pencarianDfs.name if pencarianDfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk DFS search adalah: {waktucari_dfs * 1000:.3f}")


mulaicari_bfs = time.time()
pencarianBfs = root.Bfs_search("App Version")
selesaicari_bfs = time.time()
waktucari_bfs = selesaicari_bfs - mulaicari_bfs
print(f"data ditemukan via BFS: {pencarianBfs.name if pencarianBfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk BFS search adalah: {waktucari_bfs * 1000:.3f}")