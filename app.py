# todo-list-app
tasks = [] 

def add_task(task_name): [cite: 56]
    """Thêm một công việc mới vào danh sách.""" [cite: 57]
    tasks.append(task_name) [cite: 57]
    print(f"Đã thêm công việc: '{task_name}") [cite: 60]

if __name__ == "__main__": [cite: 62, 63, 64]
    print("Chào mừng đến với ứng dụng To-Do List!") [cite: 65]
    add_task("Học bài Git và GitHub") [cite: 66]
    add_task("Làm bài tập thực hành ở nhà") [cite: 67]