import { Generation } from './Generation';
import { BenchMark } from './BenchMark';

export class GA {
    generation_count: number;
    population: number;
    crossover_rate: number;
    mutation_rate: number;
    elite_factor: number;
    generations: Generation[];
    benchmark: BenchMark;

    curr_gen: number;
    max_exec_time: number;
    max_comp_time: number;

    constructor(data: any) {
        this.curr_gen = 0;
        this.max_exec_time = -1;
        this.max_comp_time = -1;

        this.generation_count = data['generation-count'];
        this.population = data['population'];
        this.crossover_rate = data['crossover-rate'];
        this.mutation_rate = data['mutation-rate'];
        this.elite_factor = data['elite-factor'];

        this.generations = [];
        data['generations'].forEach(x => {
            let gen = new Generation(x);
            this.generations.push(gen);
            this.max_exec_time = Math.max(this.max_exec_time, gen.getWorstExecTime());
            this.max_comp_time = Math.max(this.max_comp_time, gen.getWorstCompTime());
        });
        this.benchmark = new BenchMark(data['benchmark']);
    }

    hasMoreGenerations(): boolean {
        return this.curr_gen < this.generations.length;
    }

    moveNext(): void {
        if (this.generations[this.curr_gen].hasMoreMembers()) {
            this.generations[this.curr_gen].moveNext();
        } else {
            ++this.curr_gen;
        }
    }

    getCurrentGeneration(): Generation {
        if (this.hasMoreGenerations()) {
            return this.generations[this.curr_gen];
        }
        return undefined;
    }

    getCurrentGenerationIdx() {
        return this.curr_gen;
    }

    getPreviousGen(param: string): number {
        if (this.curr_gen == 0) {
            return undefined;
        }

        switch (param) { 
            case 'AVG_FIT':
                return this.generations[this.curr_gen - 1].avg_fit;

            case 'MUTATION_COUNT':
                return this.generations[this.curr_gen - 1].mutation_count;

            case 'CROSSOVER_COUNT':
                return this.generations[this.curr_gen - 1].crossover_count;
            
            case 'FITTEST_EXEC':
                return this.generations[this.curr_gen - 1].fittest.exec_time;

            case 'FITTEST_COMP':
                return this.generations[this.curr_gen - 1].fittest.comp_time;
        }
    }

    getCurrentMemberIdx(): number {
        if (this.hasMoreGenerations()) {
            return this.generations[this.curr_gen].getCurrentMemberIdx(); 
        }
        return undefined;
    }

    getCurrentMemberExecTime(): number {
        let curr_gen = this.getCurrentGeneration();
        if (curr_gen) {
            let curr_mem = curr_gen.getCurrentMember(); 
            if (curr_mem) {
                return curr_mem.exec_time;
            }
        }
        return undefined;
    }

    getCurrentMemberCompTime(): number {
        let curr_gen = this.getCurrentGeneration();
        if (curr_gen) {
            let curr_mem = curr_gen.getCurrentMember(); 
            if (curr_mem) {
                return curr_mem.comp_time;
            }
        }
        return undefined;
    }

    reset(): void {
        this.curr_gen = 0;
        this.generations.forEach(gen => {
            gen.reset();
        });
    }

}