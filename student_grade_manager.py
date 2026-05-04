# 学生成绩管理小程序（Git实践周作业专用）
# 功能：添加学生、查看成绩、统计平均分、查找最高分
# 作者：你的名字
# 版本：v1.0

def print_menu():
    """打印主菜单"""
    print("\n===== 学生成绩管理系统 =====")
    print("1. 添加学生成绩")
    print("2. 查看所有学生成绩")
    print("3. 计算全班平均分")
    print("4. 查找最高分和最低分")
    print("5. 退出系统")
    print("6. 按姓名查询学生成绩")
    print("============================")

def add_student(students):
    """添加一名学生的成绩"""
    name = input("请输入学生姓名：")
    try:
        score = float(input("请输入学生成绩："))
        if 0 <= score <= 100:
            students[name] = score
            print(f"✅ 学生 {name} 的成绩 {score} 添加成功！")
        else:
            print("❌ 成绩必须在 0-100 之间！")
    except ValueError:
        print("❌ 输入无效，请输入数字成绩！")

def show_all(students):
    """显示所有学生成绩"""
    if not students:
        print("⚠️  暂无学生成绩记录！")
        return
    print("\n--- 所有学生成绩 ---")
    for name, score in students.items():
        print(f"{name}: {score}分")

def calc_average(students):
    """计算全班平均分"""
    if not students:
        print("⚠️  暂无数据，无法计算平均分！")
        return
    total = sum(students.values())
    avg = total / len(students)
    print(f"📊 全班平均分：{avg:.2f}分")

def find_max_min(students):
    """查找最高分和最低分"""
    if not students:
        print("⚠️  暂无数据，无法查找！")
        return
    max_score = max(students.values())
    min_score = min(students.values())
    max_students = [k for k, v in students.items() if v == max_score]
    min_students = [k for k, v in students.items() if v == min_score]
    print(f"🏆 最高分：{max_score}分，学生：{', '.join(max_students)}")
    print(f"📉 最低分：{min_score}分，学生：{', '.join(min_students)}")
def search_student(students):
    """按姓名查询学生成绩"""
    name = input("请输入要查询的学生姓名：")
    if name in students:
        print(f"✅ {name} 的成绩是：{students[name]}分")
    else:
        print(f"❌ 未找到学生 {name}！")

def main():
    students = {}  # 存储学生成绩，格式：{姓名: 成绩}
    while True:
        print_menu()
        choice = input("请输入你的选择（1-5）：")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_all(students)
        elif choice == "3":
            calc_average(students)
        elif choice == "4":
            find_max_min(students)
        elif choice == "5":
            print("👋 感谢使用，再见！")
            break
        elif choice == "6":
            search_student(students)
        else:
            print("❌ 输入无效，请输入1-5之间的数字！")

if __name__ == "__main__":
    main()