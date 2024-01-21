{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "import asyncio\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "async def get_large_data():\n",
    "    \"\"\"Асинхронная функция получения больших данных.\"\"\"\n",
    "    print(\"START: large\")\n",
    "    await asyncio.sleep(3)\n",
    "    print(\"END: large\")\n",
    "\n",
    "async def get_small_data():\n",
    "    \"\"\"Асинхронная функция получения малых данных.\"\"\"\n",
    "    print(\"START: small\")\n",
    "    await asyncio.sleep(1)\n",
    "    print(\"END: small\")\n",
    "\n",
    "async def main1():\n",
    "    \"\"\"Главная асинхронная функция вызова.\n",
    "    Не оптимальный вариант - функции выполняются последовательно.\"\"\"\n",
    "    start = time.perf_counter()\n",
    "    # Вызов асинхронных функций с помощью await\n",
    "    await get_large_data()\n",
    "    await get_small_data()\n",
    "\n",
    "    end = time.perf_counter()\n",
    "    print(f\"Заняло времени: {end-start:.2f}\")\n",
    "\n",
    "async def main2():\n",
    "    \"\"\"2-я Главная асинхронная функция вызова.\n",
    "    Тут есть оптимизация по времени. Используется функция create_task.\n",
    "    Оптимальный вариант - функции выполняются конкуретно (околопараллельно).\"\"\"\n",
    "    start = time.perf_counter()\n",
    "    # В create_tak передаем корутину get_large_data()\n",
    "    task1 = asyncio.create_task(get_large_data())\n",
    "    task2 = asyncio.create_task(get_small_data())\n",
    "    await task1\n",
    "    await task2\n",
    "\n",
    "    end = time.perf_counter()\n",
    "    print(f\"Заняло времени: {end-start:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "START: large\n",
      "END: large\n",
      "START: small\n",
      "END: small\n",
      "Заняло времени: 4.00\n"
     ]
    }
   ],
   "source": [
    "await main1()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "START: large\n",
    "END: large\n",
    "START: small\n",
    "END: small\n",
    "Заняло времени: 4.02"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "START: large\n",
      "START: small\n",
      "END: small\n",
      "END: large\n",
      "Заняло времени: 3.00\n"
     ]
    }
   ],
   "source": [
    "await main2()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "START: large\n",
    "START: small\n",
    "END: small\n",
    "END: large\n",
    "Заняло времени: 3.02"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
