import { Generation } from './Generation';
import { BenchMark } from './BenchMark';

export class GA {
    generation_count: Number;
    population: Number;
    crossover_rate: Number;
    mutation_rate: Number;
    elite_factor: Number;
    generations: Generation[];
    benchmark: BenchMark;
}