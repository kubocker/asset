import { Component } from '@angular/core';

/**
 * Generated class for the Numbers4Component component.
 *
 * See https://angular.io/api/core/Component for more info on Angular
 * Components.
 */
@Component({
  selector: 'numbers4',
  templateUrl: 'numbers4.html'
})
export class Numbers4Component {

  text: string;

  constructor() {
    console.log('Hello Numbers4Component Component');
    this.text = 'Hello World';
  }

}
