from employee import Employee


class Designer(Employee):
    def __init__(self, name):
        super().__init__(name, 4)

    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        self.seniority += 1

        # условие повышения сотрудника
        if self.seniority % 7 == 0:
            self.grade_up()

        # публикация результатов
        return self.publish_grade()
