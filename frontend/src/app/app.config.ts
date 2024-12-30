import {
  ApplicationConfig,
  importProvidersFrom,
  inject,
  provideAppInitializer,
  provideZoneChangeDetection
} from '@angular/core';
import {
  provideRouter,
  withInMemoryScrolling,
  withRouterConfig,
  withViewTransitions
} from '@angular/router';

import { routes } from './app.routes';
import { HttpClient, provideHttpClient, withInterceptors } from "@angular/common/http";
import {
  provideTranslateService,
  TranslateLoader,
  TranslateModule,
  TranslateService
} from "@ngx-translate/core";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { BrowserModule } from "@angular/platform-browser";
import { TranslateHttpLoader } from "@ngx-translate/http-loader";
import { jsonInterceptor } from "@interceptors/json.interceptor";
import { jwtInterceptor } from "@interceptors/jwt.interceptor";
import { JwtModule } from "@auth0/angular-jwt";
import { AuthService } from "@services/auth.service";
import { firstValueFrom, tap } from "rxjs";
import { TokenService } from "@services/token.service";
import { environment } from "@environments/environment";

export function httpLoaderFactory(http: HttpClient): TranslateHttpLoader {
  return new TranslateHttpLoader(http, 'i18n/', ".json");
}

export function initializerFactory(authService: AuthService) {
  return () => authService.refreshToken();
}

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({
      eventCoalescing: true
    }),
    provideRouter(
        routes,
        withViewTransitions(),
        withRouterConfig({
          onSameUrlNavigation: 'reload',
        }),
        withInMemoryScrolling({
          anchorScrolling: 'enabled'
        })
    ),
    provideAppInitializer(() => {
      const http = inject(HttpClient);
      const tokenService = inject(TokenService);
      const refresh_token = tokenService.getToken('refresh');
      console.log(refresh_token);
      if (!refresh_token) {
        return;
      }
      //const authService = inject(AuthService);
      // return authService.refreshToken().subscribe({
      //   next: (response: any) => {
      //
      //   },
      //   error: (err: any) => {
      //     console.error(err);
      //   }
      // });
      return firstValueFrom(
          http.post(`${environment.apiUrl}/api/auth/refresh_token/`, {refresh: refresh_token})
              .pipe(
                  tap(user => {
                    console.log(user);
                  })
              )
      );
    }
    ),
    provideHttpClient(
        withInterceptors([
          jsonInterceptor,
          jwtInterceptor
        ])
    ),
    provideTranslateService({
      defaultLanguage: 'hu'
    }),
    importProvidersFrom(
        BrowserModule,
        BrowserAnimationsModule,
        TranslateService,
        TranslateModule.forRoot({
          loader: {
            provide: TranslateLoader,
            useFactory: httpLoaderFactory,
            deps: [HttpClient]
          }
        }),
        JwtModule.forRoot({
          config: {
            tokenGetter: () => localStorage.getItem('token')
          }
        })
    )
  ]
};
