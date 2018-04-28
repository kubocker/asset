import { NgModule, CUSTOM_ELEMENTS_SCHEMA, NO_ERRORS_SCHEMA } from '@angular/core';
import { IonicApp, IonicModule } from 'ionic-angular';
import { Numbers3Component } from './numbers3/numbers3';
import { Numbers4Component } from './numbers4/numbers4';
import { Loto6Component } from './loto6/loto6';


import 'hammerjs';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {
  MatCheckboxModule,
  MatRadioModule,
  MatCardModule,
  MatInputModule,
  MatTableDataSource,
} from '@angular/material';

@NgModule({
	declarations: [
        Numbers3Component,
        Numbers4Component,
        Loto6Component
    ],
    imports: [
        IonicModule,
        // MatTableDataSource
    ],
    bootstrap: [IonicApp],
	exports: [Numbers3Component,
    Numbers4Component,
    Loto6Component],
    schemas: [ CUSTOM_ELEMENTS_SCHEMA, NO_ERRORS_SCHEMA ]
})
export class ComponentsModule {}
