# -*- coding: utf-8 -*-

## Aplikasi genetic algorithm untuk memenuhi tugas besar mata kuliah kecerdasan buatan
## Dibuat oleh Kelompok 11: Daniyal Arshaq Sudrajat, Riziq Rizwan.

##  =========== HAL YANG HARUS ANDA ANALISIS DAN DESAIN ===========
    ##  Ukuran populasi, rancangan kromosom, dan cara decode-nya
    ##  Metode pemilihan orangtua
    ##  Metode operasi genetik (pindah silang dan mutasi)
    ##  Probabilitas operasi genetik (𝑃𝑐 dan 𝑃𝑚)
    ##  Metode pergantian generasi (seleksi survivor)
    ##  Kriteria penghentian evolusi (loop)

##  =========== OUTPUT PROGRAM ===========
##  Dengan masalah yang didefinisikan di atas, output dari program Anda:
    ##  kromosom terbaik, dan
    ##  nilai 𝒙𝟏 dan 𝒙𝟐 hasil dekode kromosom terbaik tersebut.

##  =========== PEMBAGIAN TUGAS ===========
##  Sistem 50/50
##  Daniyal: 
    ## pendefinisian konstanta
    ## fungsi_matematis()
    ## insialisasi_populasi()
    ## dekode_kromosom()
    ## fitness()
##  Riziq:
    ## selection()
    ## crossover():
    ## mutation():
    ## generation_switch():
    ## main():

## 1. Definisi Tugas
## Diberikan suatu fungsi untuk mencari nilai 𝑥1 dan 𝑥2 sehingga diperoleh nilai minimum dari fungsi matematis berikut:
## 𝑓(𝑥1, 𝑥2) = − (𝑠𝑖𝑛(𝑥1)𝑐𝑜𝑠(𝑥2)tan(𝑥1 + 𝑥2) + 3/4 𝑒𝑥𝑝 (1 − √𝑥1^2)) dengan domain (batas nilai) untuk 𝑥1 dan 𝑥2 adalah −10 ≤ 𝑥1 ≤ 10 dan −10 ≤ 𝑥2 ≤ 10

## Buatlah program menggunakan Algoritma Genetika (GA) untuk menyelesaikan permasalahan di atas. Program menggunakan Python, 
## dan tidak diperbolehkan menggunakan Library yang secara langsung melakukan proses-proses pada GA, 
## sebagaimana tercantum pada deskripsi Case Based. Lakukan analisis dan desain program GA yang Anda buat, lalu implementasikan dengan tepat.

## Hal yang harus Anda analisis dan desain:
    ## Ukuran populasi, rancangan kromosom, dan cara decode-nya
    ## Metode pemilihan orangtua
    ## Metode operasi genetik (pindah silang dan mutasi)
    ## Probabilitas operasi genetik (𝑃𝑐 dan 𝑃𝑚)
    ## Metode pergantian generasi (seleksi survivor)
    ## Kriteria penghentian evolusi (loop)

## Proses yang harus Anda bangun/implementasikan ke dalam baris-baris program:
    ## Inisialisasi populasi
    ## Dekode kromosom
    ## Perhitungan fitness
    ## Pemilihan orangtua
    ## Crossover (pindah silang)
    ## Mutasi
    ## Pergantian Generasi
## Catatan: Proses-proses di atas harus dibangun tanpa menggunakan Library!

## 2. Output Program
## Dengan masalah yang didefinisikan di atas, output dari program Anda:
    ## kromosom terbaik, dan
    ## nilai 𝒙𝟏 dan 𝒙𝟐 hasil dekode kromosom terbaik tersebut

## ================================================================================================================== 
##                                                 PROGRAM
## ================================================================================================================== 

import random
import math

# konstanta
PANJANG_KROMOSOM = 20 # panjang kromosom binary
BIT_PER_VAR = 10 # variable x1 dan x2 direpresentasikan dengan 10 bit dalam kromosaom binary
POPULATION_SIZE = 50 # ukuran populasi
P_C = 0.8 # propability crossover
P_M = 0.01 # propability mutation
GENERASI = 100 # jumlah generasi

# fungsi matematis untuk mencari nilai 𝑥1 dan 𝑥2 sehingga diperoleh nilai minimum
def fungsi_matematis(x1, x2):
    try:
        return - (math.sin(x1) * math.cos(x2) * math.tan(x1 + x2) + (3 / 4) * math.exp(1 - math.sqrt(x1 ** 2)))
    except:
        return float('inf')

#inisialiasi populasi
def insialisasi_populasi():
    # menggunakan library random dari python untuk membuat kromosom binary berjumlah POPULATION_SIZE, atau 30 
    return [''.join(random.choice('01') for _ in range(PANJANG_KROMOSOM)) for _ in range(POPULATION_SIZE)]

#dekode kromosom
def dekode_kromosom(kromosom):
    #kromosom 20 bit dibagi menjadi dua bagian 10 bit
    x1_binary = kromosom[:BIT_PER_VAR] #ambil 10 bit pertama sebagai x1
    x2_binary = kromosom[BIT_PER_VAR:] #ambil 10 bit pertama sebagai x2

    #ubah biner ke desimal
    x1_desimal = int(x1_binary, 2) #ubah dari biner ke integer
    x2_desimal = int(x2_binary, 2) #ubah dari biner ke integer

    #skala ke rentang [-10, 10]
    #menggunakan linear scaling formula = nilai = batas_bawah + (range * desimal / (maksimum_desimal))
    # xmin = -10
    # range = 20 bit
    # maksimum_desimal = 2^20 - 1 = 1023
    x1 = -10 + (20 * x1_desimal / (2**BIT_PER_VAR - 1))
    x2 = -10 + (20 * x2_desimal / (2**BIT_PER_VAR - 1))

    return x1, x2

#perhitungan fitness
def fitness(populasi)
    fitness_values = []
    for kromosom in populasi:
        # dekode kromosom menjadi nilai x1 dan x2 rentang [-10, 10]
        x1, x2 = dekode_kromosom(kromosom)
        # hitung nilai fitness berdasarkan x1 dan x2
        fungsi = fungsi_matematis(x1, x2)
        #menambahkan satu item ke list
        fitness_values.append((kromosom, x1, x2, fungsi))
    return fitness_values

def selection(fitness_values, tournament_size=3):
    selected_parents = []
    
    for _ in range(POPULATION_SIZE):
        # Pilih kandidat secara acak untuk turnamen
        tournament_candidates = random.sample(fitness_values, tournament_size)
        
        # Urutkan kandidat berdasarkan nilai fitness (dari terkecil ke terbesar karena minimization problem)
        tournament_candidates.sort(key=lambda x: x[3])
        
        # Pilih kromosom dengan fitness terbaik (terkecil)
        selected_parents.append(tournament_candidates[0][0])
    
    return selected_parents

# Crossover (pindah silang) dengan single-point crossover
def crossover(parents):
    offspring = []
    
    # Pastikan jumlah parents genap
    if len(parents) % 2 != 0:
        parents.append(parents[0])
    
    # Lakukan crossover untuk setiap pasangan parent
    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i+1]
        
        # Peluang crossover
        if random.random() < P_C:
            # Pilih titik crossover secara acak
            crossover_point = random.randint(1, PANJANG_KROMOSOM - 1)
            
            # Buat anak dari hasil crossover
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            
            offspring.append(child1)
            offspring.append(child2)
        else:
            # Jika tidak terjadi crossover, orang tua diteruskan sebagai anak
            offspring.append(parent1)
            offspring.append(parent2)
    
    return offspring

# mutasi
def mutation(offspring):
    mutated_offspring = []
    
    for individual in offspring:
        # Ubah string menjadi list agar bisa dimodifikasi
        individual_list = list(individual)
        
        # Peluang mutasi untuk setiap bit
        for i in range(len(individual_list)):
            if random.random() < P_M:
                # Flip bit (ubah 0 jadi 1 atau 1 jadi 0)
                individual_list[i] = '1' if individual_list[i] == '0' else '0'
        
        # Ubah kembali ke string
        mutated_individual = ''.join(individual_list)
        mutated_offspring.append(mutated_individual)
    
    return mutated_offspring

# penggantian generasi dengan elitism
def generation_switch(current_population, offspring, elitism_count=2):
    # Hitung fitness untuk populasi saat ini
    current_fitness = fitness(current_population)
    
    # Urutkan berdasarkan nilai fitness (dari terkecil ke terbesar karena minimization problem)
    current_fitness.sort(key=lambda x: x[3])
    
    # Ambil beberapa individu terbaik (elitism)
    elites = [individual[0] for individual in current_fitness[:elitism_count]]
    
    # Hitung fitness untuk offspring
    offspring_fitness = fitness(offspring)
    
    # Urutkan berdasarkan nilai fitness
    offspring_fitness.sort(key=lambda x: x[3])
    
    # Buat populasi baru dengan elites dan offspring terbaik
    new_population = elites + [individual[0] for individual in offspring_fitness[:POPULATION_SIZE - elitism_count]]
    
    return new_population
    

#main function
def main():
    # inisialisasi populasi awal
    populasi = insialisasi_populasi()
    print("Populasi Awal:")
    for i, kromosom in enumerate(populasi, start=1):
        print(f"{i:2d}: {kromosom}")
    
    # Analisis populasi awal
    fitness_pop = fitness(populasi)
    print("\nFitness awal:")
    for krom, x1, x2, funct in fitness_pop:
        print(f"Kromosom: {krom}, x1: {x1:.4f}, x2: {x2:.4f}, Fitness: {funct:.4f}")
    
    # Simpan individu terbaik di setiap generasi
    best_individuals = []
    best_individual = get_best_individual(populasi)
    best_individuals.append(best_individual)
    
    # Proses evolusi
    for generasi in range(GENERASI):
        # Seleksi parents
        parents = selection(fitness(populasi))
        
        # Crossover
        offspring = crossover(parents)
        
        # Mutasi
        mutated_offspring = mutation(offspring)
        
        # Ganti generasi
        populasi = generation_switch(populasi, mutated_offspring)
        
        # Catat individu terbaik
        best_individual = get_best_individual(populasi)
        best_individuals.append(best_individual)
        
        # Cetak progress setiap 10 generasi
        if (generasi + 1) % 10 == 0:
            print(f"\nGenerasi {generasi + 1}:")
            print(f"Best fitness: {best_individual[3]:.6f}, x1: {best_individual[1]:.6f}, x2: {best_individual[2]:.6f}")
    
    # Cetak hasil akhir
    print("\nHasil Akhir setelah", GENERASI, "generasi:")
    final_best = best_individuals[-1]
    print(f"Kromosom: {final_best[0]}")
    print(f"x1: {final_best[1]:.6f}")
    print(f"x2: {final_best[2]:.6f}")
    print(f"Fitness: {final_best[3]:.6f}")
    
    # Grafik konvergensi (nilai fitness terbaik di setiap generasi)
    best_fitness_values = [ind[3] for ind in best_individuals]
    print("\nProgres Nilai Fitness Terbaik per Generasi:")
    for i, fitness_value in enumerate(best_fitness_values):
        if i % 10 == 0 or i == len(best_fitness_values) - 1:
            print(f"Generasi {i}: {fitness_value:.6f}")

if __name__ == "__main__":
    main()

