import { Component, inject, Renderer2 } from '@angular/core';
import { NgIf } from "@angular/common";

@Component({
  selector: 'app-navbar',
  imports: [
    NgIf
  ],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent {

  renderer: any = inject(Renderer2);
  isLoggedIn: boolean = false;
  dropdownOpen: any;
  mobileMenuOpen: any;
  darkMode: boolean = true;

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
}
