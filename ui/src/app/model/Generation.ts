import { Member } from './Member';

export class Generation {
    members: Member[];
    avg_fit: Number;
    fittest: Member;
    mutation_count: Number;
    crossover_count: Number;
}