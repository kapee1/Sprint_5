from selenium.webdriver.common.by import By


class StellarBurgerLocators:
    NAME_FIELD = By.XPATH, ".//label[text() = 'Имя']/../input"  # Поле имя на странице регистрации
    EMAIL_FIELD = By.XPATH, ".//label[text() = 'Email']/../input"  # Поле email на странице регистрации
    PASSWORD_FIELD = By.XPATH, ".//label[text() = 'Пароль']/../input"  # Поле пароль на странице регистрации

    REGISTER_BUTTON = By.XPATH, ".//button[text () = 'Зарегистрироваться']"

    LOGIN_BUTTON_ON_LOGIN_PAGE = By.XPATH, ".//button[text() = 'Войти']"
    LOGIN_BUTTON_ON_MAIN_PAGE = By.XPATH, ".//button[text()='Войти в аккаунт']"
    LOGIN_BUTTON_IN_HINT = By.XPATH, ".//a[text()='Войти']"

    PROFILE_BUTTON_ON_MAIN_PAGE = By.XPATH, ".//p[text()='Личный Кабинет']"

    USER_ALREADY_EXIST_WARNING = By.XPATH, ".//p[text() = 'Такой пользователь уже существует']"
    INCORRECT_PASSWORD_WARNING = By.XPATH, ".//p[text()='Некорректный пароль']"

    LOGO_IN_HEADER = By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']"
    LOG_OUT_BUTTON_IN_PROFILE = By.XPATH, ".//button[text() = 'Выход']"

    CAPTION_FOR_SECTION_BUNS = By.XPATH, ".//h2[text()= 'Булки']"
    CAPTION_FOR_SECTION_SAUCES = By.XPATH, ".//h2[text()= 'Соусы']"
    CAPTION_FOR_SECTION_FILLINGS = By.XPATH, ".//h2[text()= 'Начинки']"

    BUNS_IN_SECTION_SELECTOR = By.XPATH, ".//span[text() = 'Булки']"
    PARENT_BUNS_IN_SECTION_SELECTOR = By.XPATH, ".//span[text() = 'Булки']/parent::div"

    FILLINGS_IN_SECTION_SELECTOR = By.XPATH, ".//span[text() = 'Начинки']"
    PARENT_FILLINGS_IN_SECTION_SELECTOR = By.XPATH, ".//span[text() = 'Начинки']/parent::div"

    SAUCES_IN_SECTION_SELECTOR = By.XPATH, ".//span[text() = 'Соусы']"
    PARENT_SAUCES_IN_SECTION_SELECTOR = By.XPATH, ".//span[text() = 'Соусы']/parent::div"
