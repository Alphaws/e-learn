import { inject, Injectable, signal, WritableSignal } from '@angular/core';
import { HttpClient, HttpContext } from "@angular/common/http";
import { environment } from "@environments/environment";
import { catchError, map, Observable, of, pipe } from "rxjs";
import { Login, LoginResponse, User } from "@interfaces/login.interface";
import { IS_PUBLIC } from "@interceptors/jwt.interceptor";
import { JwtHelperService } from "@auth0/angular-jwt";
import { Router } from "@angular/router";
import { TokenService } from "@services/token.service";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  http = inject(HttpClient);
  router = inject(Router);
  tokenService = inject(TokenService);
  jwtHelper = inject(JwtHelperService);

  #user: WritableSignal<User | null> = signal<User | null>(null);
  user: any = this.#user.asReadonly();

  apiUrl = environment.apiUrl;
  CONTEXT = {context: new HttpContext().set(IS_PUBLIC, true)};

  //get user(): WritableSignal<User | null> {
  //const token = this.tokenService.getToken();
  //return signal(token ? this.jwtHelper.decodeToken(token) : null);
  //}

  constructor() { }

  isAuthenticated(): boolean {
    return !this.jwtHelper.isTokenExpired();
  }

  login(loginData: Login): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(
        `${this.apiUrl}/api/auth/login/`,
        loginData,
        this.CONTEXT
    ).pipe(
            catchError(error => {
              if (error.status === 401) {
                console.error('Invalid credentials');
              }
              return of();
            }),
            map((response: LoginResponse) => {
              if ('user' in response) {
                this.#user.set(response.user);
                this.tokenService.setToken(response.access_token);
                this.tokenService.setToken(response.refresh_token, 'refresh');
              }
              console.log('RESPONSE:', response);
              return response;
            })

        );
  }

  logout() {
    this.router.navigate(['/']);
  }

  getProfileData() {
    return this.http.get(`${this.apiUrl}/api/auth/profile/`, {withCredentials: true});
  }

  register(registerData: any) {
    return this.http.post(this.apiUrl + '/api/auth/register/', registerData);
  }

  forgotPassword(email: string) {}

  resetPassword(email: string, password: string, code: string) {}

  refreshToken() {
    const refresh_token = this.tokenService.getToken('refresh');
    if (!refresh_token) {
      return of();
    }
    return this.http.post<LoginResponse>(`${this.apiUrl}/api/auth/refresh_token/`, {refresh: refresh_token}, {withCredentials: true})
        .pipe(
            map((response: LoginResponse) => {
              if ('user' in response) {
                this.#user.set(response.user);
              }
              return response;
            })
        );
  }
}
