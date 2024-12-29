import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TokenService {

  private ACCESS_TOKEN_KEY: string = 'accessToken';
  private REFRESH_TOKEN_KEY: string = 'refreshToken';

  private TOKEN_KEY_PAIRS: Record<string, string> = {
    'access': this.ACCESS_TOKEN_KEY,
    'refresh': this.REFRESH_TOKEN_KEY
  };

  constructor() { }

  public setToken(token: string, type: string = 'access'): void {
    const key = this.TOKEN_KEY_PAIRS[type];
    sessionStorage.setItem(key, token);
  }

  public getToken(type: string = 'access'): string | null {
    const key = this.TOKEN_KEY_PAIRS[type];
    return sessionStorage.getItem(key);
  }

  public removeToken(type: string = 'access'): void {
    const key = this.TOKEN_KEY_PAIRS[type];
    sessionStorage.removeItem(key);
  }
}
