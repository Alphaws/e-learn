import { Component, inject, OnInit, Renderer2 } from '@angular/core';
import { CommonModule, NgIf } from "@angular/common";

import { FormsModule } from "@angular/forms";
import { TranslateModule, TranslatePipe, TranslateService } from "@ngx-translate/core";
import { LanguageService } from "@services/language.service";
import { RouterLink } from "@angular/router";
import { LoginModalComponent } from "@modules/auth/login-modal/login-modal.component";
import { AuthService } from "@services/auth.service";
import { environment } from "@environments/environment";

@Component({
  selector: 'app-navbar',
  imports: [
    NgIf,
    FormsModule,
    RouterLink,
    LoginModalComponent,
    CommonModule,
    TranslatePipe,
  ],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent implements OnInit{

  renderer: any = inject(Renderer2);
  translate = inject(TranslateModule);
  translateService = inject(TranslateService);
  languageService = inject(LanguageService);
  authService = inject(AuthService);
  isLoggedIn: boolean = false;
  dropdownOpen: any;
  mobileMenuOpen: any;
  darkMode: boolean = true;
  selectedLanguage: any;
  languageDropdownOpen: boolean = false;

  user = this.authService.user;

  constructor() {
    this.isLoggedIn = false;
    this.dropdownOpen = false;
    this.mobileMenuOpen = false;
    this.darkMode = true;
    this.selectedLanguage = this.languageService.getLanguage();
    this.translateService.setDefaultLang('hu');
    this.translateService.use(this.selectedLanguage);
  }

  ngOnInit() {
    // const token = localStorage.getItem('jwt');
    // console.log('Token:', token);
    // if (token) {
    //   this.isLoggedIn = true; // Token alapján automatikusan bejelentkezve marad
    // }
  }

  toggleMobileMenu() {
    this.mobileMenuOpen = !this.mobileMenuOpen;

  }

  toggleDropdown() {
    this.dropdownOpen = !this.dropdownOpen;

  }

  logout() {
    this.isLoggedIn = false;
    this.mobileMenuOpen = false;
    this.authService.logout();
  }

  toggleDarkMode() {
    const html = document.documentElement;
    if (html.classList.contains('dark')) {
      this.renderer.removeClass(html, 'dark');
    } else {
      this.renderer.addClass(html, 'dark');
    }
  }

  changeLanguage(lang: string | null) {
    this.selectedLanguage = lang;
    if (lang) {
      this.translateService.use(lang);
      this.languageService.setLanguage(lang);
      this.languageDropdownOpen = false
      return lang;
    }
    this.translateService.use(this.selectedLanguage);
    this.languageService.setLanguage(this.selectedLanguage);
    this.languageDropdownOpen = false;
    return this.selectedLanguage;

  }

  onLoginSuccess() {
    //this.isLoggedIn = true;
  }

  toggleLanguageDropdown() {
    this.languageDropdownOpen = !this.languageDropdownOpen;
  }

  protected readonly environment = environment;

  getSelectedLanguageImage() {
    const languageImages: { [key: string]: string } = {
      en: 'assets/images/flags/gb.svg',
      hu: 'assets/images/flags/hu.svg',
      de: 'assets/images/flags/de.svg',
      ru: 'assets/images/flags/ru.svg'
    };
    const selectedLanguage = this.selectedLanguage || this.languageService.getLanguage();
    return languageImages[selectedLanguage] || 'assets/images/flags/hu.svg';
  }
}
