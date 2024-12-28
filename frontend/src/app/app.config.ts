import {
  ApplicationConfig,
  importProvidersFrom,
  provideZoneChangeDetection
} from '@angular/core';
import { provideRouter, withInMemoryScrolling, withRouterConfig, withViewTransitions } from '@angular/router';

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

export function httpLoaderFactory(http: HttpClient): TranslateHttpLoader {
  return new TranslateHttpLoader(http, 'i18n/', ".json");
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
        })
    )
  ]
};
