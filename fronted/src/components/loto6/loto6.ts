import { Component } from '@angular/core';

/**
 * Generated class for the Loto6Component component.
 *
 * See https://angular.io/api/core/Component for more info on Angular
 * Components.
 */
@Component({
  selector: 'loto6',
  templateUrl: 'loto6.html'
})
export class Loto6Component {

  text: string;

  constructor() {
    console.log('Hello Loto6Component Component');
    this.text = 'Hello World';
  }

}
