import {
    Entity,
    PrimaryGeneratedColumn,
    Column
} from "typeorm";

@Entity()
export class Numbers {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    title: string;

    @Column()
    date: string;

    @Column()
    numbers3: string;

    @Column()
    numbers4: string;

    @Column()
    calendar: string;

    @Column()
    week: string;
}
