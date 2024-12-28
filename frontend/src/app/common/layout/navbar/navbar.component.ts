import { Component, inject, OnInit, Renderer2 } from '@angular/core';
import { NgIf } from "@angular/common";
import { FormsModule } from "@angular/forms";
import { TranslateModule, TranslatePipe, TranslateService } from "@ngx-translate/core";
import { LanguageService } from "@services/language.service";
import { RouterLink } from "@angular/router";
import { LoginModalComponent } from "@modules/auth/login-modal/login-modal.component";

@Component({
  selector: 'app-navbar',
  imports: [
    NgIf,
    FormsModule,
    RouterLink,
    LoginModalComponent,
    TranslatePipe
  ],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent implements OnInit{

  renderer: any = inject(Renderer2);
  translate = inject(TranslateModule);
  translateService = inject(TranslateService);
  languageService = inject(LanguageService);
  isLoggedIn: boolean = false;
  dropdownOpen: any;
  mobileMenuOpen: any;
  darkMode: boolean = true;
  selectedLanguage: any;

  constructor() {
    this.isLoggedIn = false;
    this.dropdownOpen = false;
    this.mobileMenuOpen = false;
    this.darkMode = true;
    this.selectedLanguage = this.languageService.getLanguage();
    //this.selectedLanguage = 'hu';
    this.translateService.setDefaultLang('hu');
    this.translateService.use(this.selectedLanguage);
  }

  ngOnInit() {
    const token = localStorage.getItem('jwt');
    if (token) {
      this.isLoggedIn = true; // Token alapján automatikusan bejelentkezve marad
    }
  }

  toggleMobileMenu() {
    this.mobileMenuOpen = !this.mobileMenuOpen;

  }

  toggleDropdown() {
    this.dropdownOpen = !this.dropdownOpen;

  }

  logout() {
    // Kilépési logika
    console.log('User logged out');
    this.isLoggedIn = false;
    this.mobileMenuOpen = false; // Zárja be a mobilmenüt is
  }

  //login() {

    //this.isLoggedIn = true;
  //}

  toggleDarkMode() {
    const html = document.documentElement;
    if (html.classList.contains('dark')) {
      this.renderer.removeClass(html, 'dark');
    } else {
      this.renderer.addClass(html, 'dark');
    }
  }

  changeLanguage(lang: string | null) {
    if (lang) {
      this.translateService.use(lang);
      this.languageService.setLanguage(lang);
      return lang;
    }
    this.translateService.use(this.selectedLanguage);
    this.languageService.setLanguage(this.selectedLanguage);
    return this.selectedLanguage;

  }

  onLoginSuccess() {
    this.isLoggedIn = true;
  }
}
