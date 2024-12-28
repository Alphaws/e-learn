import { Component, OnInit, EventEmitter, Output, inject } from '@angular/core';
import { JsonPipe, NgIf } from "@angular/common";
import { FormsModule } from "@angular/forms";
import { TranslatePipe } from "@ngx-translate/core";
import { AuthService } from "@services/auth.service";

@Component({
  selector: 'app-login-modal',
  imports: [
    NgIf,
    FormsModule,
    TranslatePipe,
  ],
  templateUrl: './login-modal.component.html',
  styleUrl: './login-modal.component.scss'
})
export class LoginModalComponent implements OnInit{

  authService: any = inject(AuthService);
  isVisible: boolean = false;
  credentials = { email: '', password: '' };

  @Output() loginSuccess = new EventEmitter<void>();

  constructor() {}

  ngOnInit() {}

  open() {
    this.isVisible = true;
  }

  close() {
    this.isVisible = false;
  }

  onLogin() {
    this.authService.login(this.credentials).subscribe({
      next: (response: any) => {
        console.log(response);
        this.loginSuccess.emit();
        this.close();
      },
      error: (err: any) => {
        console.log(err);
      }
    });
  }
}
