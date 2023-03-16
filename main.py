
# Класс Person:
# свойства: ИНН, Адрес
class Person:
    def __init__(self, inn, address):
        self.inn = inn
        self.address = address


# Класс Individual (Физическое лицо, наследуется от Person):
# свойства: Фамилия, Имя, Отчество, Доход, Ставка налога
# методы:
# рассчитать подоходный налог (calculate_income_tax) - возвращает сумму подоходного налога в рублях,
# рассчитанную как произведение дохода на ставку налога (13%)
class Individual(Person):
    def __init__(self, inn, address, last_name, first_name, middle_name, income, tax_rate):
        super().__init__(inn, address)
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.income = income
        self.tax_rate = tax_rate

    def calculate_income_tax(self):
        return self.income * self.tax_rate


# Класс LegalEntity (Юридическое лицо, наследуется от Person):
# свойства: Название, Доход, Расход, Ставка налога, Тип УСН
# методы:
# рассчитать налог (calculate_tax) - возвращает сумму налога в рублях, рассчитанную в зависимости от типа УСН:
# если "УСН доходы минус расходы", то налог рассчитывается как произведение разности дохода и
# расхода на ставку налога (6%)
# если "УСН доходы", то налог рассчитывается как произведение дохода на ставку налога (15%)
class LegalEntity(Person):
    def __init__(self, inn, address, name, income, expenses, tax_rate, usn_type):
        super().__init__(inn, address)
        self.name = name
        self.income = income
        self.expenses = expenses
        self.tax_rate = tax_rate
        self.usn_type = usn_type

    def calculate_tax(self):
        if self.usn_type == "УСН доходы минус расходы":
            return (self.income - self.expenses) * self.tax_rate
        elif self.usn_type == "УСН доходы":
            return self.income * self.tax_rate


# Класс PersonList (Список лиц):
# свойства: список физических лиц, список юридических лиц
# методы:
# рассчитать суммарную величину налога Физлиц (calculate_total_income_tax_for_individuals) -
# возвращает сумму подоходного налога в рублях, рассчитанную для всех физических лиц в списке
# рассчитать суммарную величину налога Юрлиц (calculate_total_income_tax_for_legal_entities) -
# возвращает сумму налога в рублях, рассчитанную для всех юридических лиц в списке
class PersonList:
    def __init__(self, individuals, legal_entities):
        self.individuals = individuals
        self.legal_entities = legal_entities

    def calculate_total_income_tax_for_individuals(self):
        total_income_tax = 0
        for individual in self.individuals:
            total_income_tax += individual.calculate_income_tax()
        return total_income_tax

    def calculate_total_tax_for_legal_entities(self):
        total_tax = 0
        for legal_entity in self.legal_entities:
            total_tax += legal_entity.calculate_tax()
        return total_tax
