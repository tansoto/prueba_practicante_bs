import { Component } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent {
    
  
    nombre_pokemon: string = 'pikachu'; // or the appropriate type
    constructor() { }
}
