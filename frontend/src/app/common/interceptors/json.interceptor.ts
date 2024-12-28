import { HttpInterceptorFn } from '@angular/common/http';

export const jsonInterceptor: HttpInterceptorFn = (req, next) => {
  req = req.clone({
    headers: req.headers.set('Content-Type', 'application/json')
  })
  return next(req);
};
