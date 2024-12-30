import { Injectable, signal, WritableSignal } from '@angular/core';
@Injectable({
  providedIn: 'root'
})
export class LanguageService {
  private availableLanguages = ['en', 'hu', 'de', 'ru'];  // Elérhető nyelvek
  private defaultLanguage = 'hu';  // Alapértelmezett nyelv

  language :WritableSignal<string> = signal(this.getLanguage());

  constructor() { }

  setLanguage(language: string): void {
    if (this.availableLanguages.includes(language)) {
      localStorage.setItem('language', language);
      this.language.set(language);
    } else {
      localStorage.setItem('language', this.defaultLanguage);
      this.language.set(this.defaultLanguage);
    }
  }

  getLanguage(): string {
    const storedLanguage = localStorage.getItem('language');
    if (storedLanguage && this.availableLanguages.includes(storedLanguage)) {
      return storedLanguage;
    }

    const browserLanguage = navigator.language.split('-')[0];  // Pl. 'en' vagy 'hu'

    return this.availableLanguages.includes(browserLanguage) ? browserLanguage : this.defaultLanguage;
  }
}
