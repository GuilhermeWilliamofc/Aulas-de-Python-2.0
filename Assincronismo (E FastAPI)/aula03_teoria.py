import asyncio

# a teoria é sobre Assincronismo na Prática

# corroutina
async def fala_oi(nome):
    print(f'\033[36m{nome} está vindo...\033[m')
    await asyncio.sleep(2) # Simulando I/O, pelo oq entendi o await é usado em toda a função async
    print(f'\033[35m{nome} falou Oi...\033[m')

# corroutina
async def main():
    await fala_oi('Larissa') # atuação sincrona, a função inicia e termina isolada
    await asyncio.gather(fala_oi('Lhama'), fala_oi('Rogério')) # atuação assincrona, a partir do momento que uma das funções precisou parar por um tempo a outra função já inicia

asyncio.run(main()) # vc "fala" para iniciar o main()
