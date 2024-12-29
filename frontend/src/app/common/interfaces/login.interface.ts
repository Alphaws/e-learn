export interface Login {
  email: string;
  password: string;
}

export interface User {
  username: string;
  firstname: string;
  lastname: string;
  roles: string[];
}

export interface LoginError {
  code: number;
  message: string;
}

export interface LoginSuccess {
  // token: string;
  // refresh_token: string;
  user: User;
  message: string;
}

export type LoginResponse = LoginSuccess | LoginError;
