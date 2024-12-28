import { inject, Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { environment } from "@environments/environment";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  http = inject(HttpClient);
  apiUrl = environment.apiUrl;

  constructor() { }

  login(loginData: any) {
    return this.http.post(this.apiUrl + 'api/auth/login/', loginData);
  }

  authenticateByToken(token: string, type: string = 'jwt') {
    return this.http.get(this.apiUrl + 'api/auth/authenticate/');
  }

  register(registerData: any) {
    return this.http.post(this.apiUrl + 'api/auth/register/', registerData);
  }

  forgotPassword(email: string) {}

  resetPassword(email: string, password: string, code: string) {}
}
