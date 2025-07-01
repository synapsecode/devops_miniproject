from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Nice App UI</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 min-h-screen flex">

    <!-- Sidebar -->
    <aside class="w-64 bg-white shadow-lg hidden sm:block">
        <div class="p-6 text-xl font-bold text-gray-800 border-b">DEVOPS PROJECT!</div>
        <nav class="p-4 space-y-2">
            <a href="#" class="block px-4 py-2 rounded hover:bg-gray-100">Dashboard</a>
            <a href="#" class="block px-4 py-2 rounded hover:bg-gray-100">Profile</a>
            <a href="#" class="block px-4 py-2 rounded hover:bg-gray-100">Settings</a>
            <a href="#" class="block px-4 py-2 rounded hover:bg-gray-100">Logout</a>
        </nav>
    </aside>

    <!-- Main Content -->
    <div class="flex-1 flex flex-col">
        <!-- Navbar -->
        <header class="bg-white shadow p-4 flex justify-between items-center">
            <h1 class="text-xl font-semibold text-gray-700">Dashboard of 01 July! 10:30AMs</h1>
            <div class="flex items-center gap-3">
                <span class="text-sm text-gray-500">Hello, User</span>
                <img src="https://i.pravatar.cc/32" alt="User Avatar" class="rounded-full w-8 h-8" />
            </div>
        </header>

        <!-- Content -->
        <main class="p-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div class="bg-white rounded-xl shadow p-4">
                <h2 class="font-semibold text-lg text-gray-800">Card 1</h2>
                <p class="text-sm text-gray-600 mt-2">This project uses Docker, Minikube, Kubernetes, Jenkins and more</p>
            </div>
        </main>
    </div>

</body>

</html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)