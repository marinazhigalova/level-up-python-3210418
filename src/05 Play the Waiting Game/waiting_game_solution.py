import random, time

def waiting_game():
    target_sec = random.randint(2,4)
    print(f'You need to wait for exactly {target_sec} seconds to win a game!')

    input('---Press ENTER to start---')
    start_time = time.perf_counter()
    
    input('---Press ENTER to finish---')
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    if(elapsed_time == target_sec):
        print(f'You WIN the game! You waited for exactly {elapsed_time:.3f} seconds!')
    elif(elapsed_time > target_sec):
        print(f'You waited for too long! {elapsed_time - target_sec :.3f} seconds more than needed')
    elif(elapsed_time < target_sec): 
        print(f'You did not waited long enough! {target_sec - elapsed_time :.3f} seconds less than needed')

# commands used in solution video for reference
if __name__ == '__main__':
    waiting_game()




