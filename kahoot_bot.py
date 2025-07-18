import threading
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from typing import List

class ConsoleColors:
    """ANSI color codes for console output"""
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class KahootBot(threading.Thread):
    """Threaded Kahoot bot that joins games with human-like behavior"""
    
    def __init__(self, pin: str, bot_name: str, headless: bool = False):
        super().__init__()
        self.pin = pin
        self.name = bot_name
        self.headless = headless
        self.service = ChromeService(
            ChromeDriverManager().install(), 
            log_path='NUL', 
            service_args=['--log-level=OFF']
        )
        self.faker = Faker()
        self.user_agent = self.faker.user_agent()

    def _configure_browser(self) -> webdriver.Chrome:
        """Configure Chrome browser options with anti-detection measures"""
        options = webdriver.ChromeOptions()
        
        if self.headless:
            options.add_argument("--headless=new")
            
        options.add_argument("--log-level=3")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--mute-audio")
        options.add_argument(f"--window-size={random.randint(1024, 1400)},{random.randint(768, 900)}")
        options.add_argument(f'--user-agent={self.user_agent}')
        options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument(f"--lang={self.faker.language_code()}")
        options.add_argument(f"--timezone={self.faker.timezone()}")
        
        return webdriver.Chrome(service=self.service, options=options)

    def run(self):
        """Execute the bot's workflow"""
        driver = None
        try:
            driver = self._configure_browser()
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            print(f"{ConsoleColors.OKGREEN}[+] Bot '{self.name}' joining game...{ConsoleColors.ENDC}")
            time.sleep(random.uniform(0.5, 3.0))
            driver.get(f"https://kahoot.it/?pin={self.pin}")
            
            wait = WebDriverWait(driver, 15)
            name_field_selector = "#nickname, [data-functional-selector='username-input']"
            name_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, name_field_selector)))
            
            for char in self.name:
                name_field.send_keys(char)
                time.sleep(random.uniform(0.05, 0.3))
                if random.random() < 0.1:
                    name_field.send_keys(random.choice(['a', 'e', 'x', '']))
                    time.sleep(random.uniform(0.1, 0.5))
                    name_field.send_keys('\b')
            
            time.sleep(random.uniform(0.2, 1.5))
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            
            driver.execute_script("arguments[0].style.backgroundColor = 'yellow'", submit_button)
            time.sleep(random.uniform(0.1, 0.7))
            driver.execute_script("arguments[0].style.backgroundColor = ''", submit_button)
            submit_button.click()
            
            print(f"{ConsoleColors.OKGREEN}[+] Bot '{self.name}' successfully joined the game!{ConsoleColors.ENDC}")
            time.sleep(random.randint(600, 1800))

        except (WebDriverException, TimeoutException) as e:
            print(f"{ConsoleColors.FAIL}[-] Bot '{self.name}' failed to join: {str(e)}{ConsoleColors.ENDC}")
        finally:
            if driver:
                driver.quit()

def display_warning():
    """Show warning message with ASCII art"""
    warning_art = rf"""
    {ConsoleColors.FAIL}
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║  
    ║                                                                  ║  
    ║                ██╗    ██╗ █████╗ ██████╗ ███╗   ██╗              ║
    ║                ██║    ██║██╔══██╗██╔══██╗████╗  ██║              ║
    ║                ██║ █╗ ██║███████║██████╔╝██╔██╗ ██║              ║
    ║                ██║███╗██║██╔══██║██╔══██╗██║╚██╗██║              ║
    ║                ╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║              ║
    ║                 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝              ║
    ║                                                                  ║
    ║            This tool is for educational purposes only!           ║
    ║          Using this may violate Kahoot's Terms of Service.       ║
    ║          Excessive botting may get you banned from Kahoot.       ║  
    ║                                                                  ║
    ║                                                     -Team PhaZto ║
    ╚══════════════════════════════════════════════════════════════════╝

    {ConsoleColors.ENDC}
    """
    print(warning_art)
    input(f"{ConsoleColors.WARNING}Press Enter to continue or Ctrl+C to exit...{ConsoleColors.ENDC}")

def get_valid_input(prompt: str, validation_func, error_msg: str):
    """Get validated user input with retry logic"""
    while True:
        try:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            print(f"{ConsoleColors.FAIL}{error_msg}{ConsoleColors.ENDC}")
        except KeyboardInterrupt:
            print(f"\n{ConsoleColors.FAIL}Operation cancelled by user.{ConsoleColors.ENDC}")
            exit()

def validate_pin(pin: str) -> bool:
    """Validate Kahoot PIN format"""
    return pin.isdigit() and len(pin) == 6

def validate_bot_count(count: str) -> bool:
    """Validate bot count"""
    return count.isdigit() and int(count) > 0

def main():
    """Main interactive terminal interface"""
    display_warning()
    
    print(f"\n{ConsoleColors.BOLD}{ConsoleColors.OKCYAN}=== Kahoot Bot Army Configuration ==={ConsoleColors.ENDC}")
    
    # Get game PIN
    pin = get_valid_input(
        f"{ConsoleColors.OKCYAN}[?] Enter 6-digit Kahoot PIN: {ConsoleColors.ENDC}",
        validate_pin,
        "Invalid PIN! Must be exactly 6 digits."
    )
    
    # Get bot count
    num_bots = int(get_valid_input(
        f"{ConsoleColors.OKCYAN}[?] Number of bots to deploy (1-50): {ConsoleColors.ENDC}",
        validate_bot_count,
        "Invalid number! Must be positive integer."
    ))
    
    if num_bots > 20:
        print(f"{ConsoleColors.WARNING}Warning: Running more than 20 bots may strain your system!{ConsoleColors.ENDC}")
        confirm = input(f"{ConsoleColors.WARNING}Are you sure? (y/n): {ConsoleColors.ENDC}").lower()
        if confirm != 'y':
            num_bots = 20
            print(f"{ConsoleColors.OKGREEN}Using 20 bots as default.{ConsoleColors.ENDC}")
    
    # Get base name
    base_name = input(f"{ConsoleColors.OKCYAN}[?] Base name for bots (e.g., 'Student'): {ConsoleColors.ENDC}") or "Bot"
    
    # Ask about headless mode
    headless = input(f"{ConsoleColors.OKCYAN}[?] Run in headless mode? (y/n): {ConsoleColors.ENDC}").lower() == 'y'
    
    print(f"\n{ConsoleColors.BOLD}Launching {num_bots} bots with name pattern: {base_name} [1-{num_bots}]{ConsoleColors.ENDC}")
    print(f"{ConsoleColors.WARNING}Starting in 5 seconds... (Press Ctrl+C to cancel){ConsoleColors.ENDC}")
    time.sleep(5)
    
    bot_names = [f"{base_name} {i}" if num_bots > 1 else base_name for i in range(1, num_bots + 1)]
    threads = []
    
    try:
        for name in bot_names:
            bot = KahootBot(pin, name, headless)
            threads.append(bot)
            bot.start()
            time.sleep(random.uniform(0.3, 1.5))
        
        for t in threads:
            t.join()
            
    except KeyboardInterrupt:
        print(f"\n{ConsoleColors.WARNING}Shutting down all bots...{ConsoleColors.ENDC}")
    finally:
        print(f"\n{ConsoleColors.BOLD}{ConsoleColors.OKGREEN}Operation completed.{ConsoleColors.ENDC}")

if __name__ == "__main__":
    main()
