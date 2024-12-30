import { HttpContextToken, HttpInterceptorFn, HttpRequest } from '@angular/common/http';
import { inject } from "@angular/core";
import { AuthService } from "@services/auth.service";

export const jwtInterceptor: HttpInterceptorFn = (req, next) => {
  //const authService = inject(AuthService);
  if (req.context.get(IS_PUBLIC)) {
    return next(req);
  }
  const authRequest = addTokenToHeader(req);
  return next(authRequest);
};

const addTokenToHeader = (req: HttpRequest<any>):HttpRequest<any>  => {
  const token = localStorage.getItem('token');
  return req.clone({
    headers: req.headers.set('Authorization', `Bearer ${token}`)
  });
};

export const IS_PUBLIC = new HttpContextToken(() => false);
