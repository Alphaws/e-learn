import { Component, inject, Renderer2 } from '@angular/core';
import { NgIf } from "@angular/common";
import { FormsModule } from "@angular/forms";
import { TranslateModule, TranslateService } from "@ngx-translate/core";

@Component({
  selector: 'app-navbar',
  imports: [
    NgIf,
    FormsModule
  ],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent {

  renderer: any = inject(Renderer2);
  translate = inject(TranslateModule);
  translateService = inject(TranslateService);
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
    this.selectedLanguage = 'hu';
    this.selectedLanguage = 'hu';
    this.translateService.setDefaultLang('hu');
    this.translateService.use(this.selectedLanguage);
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

  login() {
    this.isLoggedIn = true;
  }

  toggleDarkMode() {
    const html = document.documentElement;
    if (html.classList.contains('dark')) {
      this.renderer.removeClass(html, 'dark');
    } else {
      this.renderer.addClass(html, 'dark');
    }
  }

  changeLanguage() {
    this.translateService.use(this.selectedLanguage);

  }
}
