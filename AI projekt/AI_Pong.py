import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train/255.0
x_test = x_test/255.0

model = Sequential()

model.add(Lstm(128, input_shape=(x_train.shape[1:]), activation='relu', return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(10, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-5)

model.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics['accuracy'])
model.fit(x_train, y_train, epochs=3, validation_data=(x_test, y_test))


# from keras.optimizers import Adam
# from keras import backend as K
# import numpy as np



# class ReplayBuffer(object):
#     def __init__(self, max_size, input_shape):
#         self.mem_size = max_size
#         self.mem_cntr = 0

#         self.state_memory = np.zeros((self.mem_size, *input_shape), dtype = np.float32)
#         self.new_state_memory = np.zeros((self.mem_size, *input_shape), dtype = np.float32)
#         self.action_memory = np.zeros(self.mem_size, dtype = np.int32)
#         self.reward_memory = np.zeros(self.mem_size, dtype = np.float32)
#         self.terminal_memory = np.zeros(self.mem_size, dtype = np.uint8)

#     def store_transition(self, state, action, reward, state_, done):
#         index = self.mem_cntr % self.mem_size
#         self.state_memory[index] = state
#         self.new_state_memory[index] = state_
#         self.reward_memory[index] = reward
#         self.action_memory[index] = action
#         self.terminal_memory[index] = done

#         self.mem_cntr += 1
    
#     def sample_buffer(self, batch_size):
#         max_mem = min(self.mem_cntr, self.mem_size)
#         batch = np.random.choice(max_mem, batch_size, replace=False)

#         states = self.state_memory[batch]
#         new_states = self.new_state_memory[batch]
#         actions = self.action_memory[batch]
#         rewards = self.reward_memory[batch]
#         dones = self.terminal_memory[batch]

#         return states, actions, rewards, new_states, dones

# def build_dqn(lr, n_actions, input_dims, fcl_dims):
#     model = Sequential()
#     model.add(Conv2D(filters=32, kernel_size=8, strides=4, activation='relu', input_shape=(*input_dims,), data_format='channels_first'))
#     model.add(Conv2D(filters=64, kernel_size=4, strides=2, activation='relu', data_format='channels_first'))
#     model.add(Conv2D(filters=64, kernel_size=3, strides=1, activation='relu', data_format='channels_first'))
#     model.add(Flatten())
#     model.add(Dense(fcl_dims, activation='relu'))
#     model.add(Dense(n_actions))

#     model.compile(optimizer=Adam(lr=lr), loss='mean_squared_error')

#     return model

# class Agent(object):
#     def __init__(self, alpha, gamma, n_actions, epsilon, batch_size, replace, input_dims, eps_dec=1e-5, eps_min=0.01, mem_size=1000000, q_eval_frame='q_eval.h5', q_target_frame='q_target.h5'):
#         self.action_space = [i for i in range(n_actions)]
#         self.gamma = gamma
#         self.epsilon = epsilon
#         self.eps_dec = eps_dec
#         self.eps_min = eps_min
#         self.batch_size = batch_size
#         self.replace = replace
#         self.q_target_model_file = q_target_fname
#         self.q_eval_model_file = q_eval_fname
#         self.learn_step = 0
#         self.memory = ReplayBuffer(mem_size, input_dims)
#         self.q_eval = build_dqn(alpha, n_actions, input_dims, 512)
#         self.q_next = build_dqn(alpha, n_actions, input_dims, 512)

#     def replace_target_network(self):
#         if self.replace != 0 and self.learn_step % self.replace == 0:
#             self.q_next.set_weights(self.q_eval.get_weights())

#     def store_transition(self, state, action, reward, new_state, done):
#         self.memory.store_transition(state, action, reward, new_state, done)
    
#     def choose_action(self, observation):
#         if np.random.choice() < self.epsilon:
#             action = np.random.choice(self.action_space)
#         else:
#             state = np.array([observation], copy=False, dtype=np.float32)
#             actions = self.q_eval.predict(state)
#             action = np.argmax(actions)

#         return action

#     def learn(self):
#         if self.memory.mem_cntr > self.batch_size:
#             state, action, reward, new_state, done = self.memory.sample_buffer(self.batch_size)

#             self.replace_target_network()

#             q_eval = self.q_eval.predict(state)
#             q_next = self.q_next.predict(new_state)

#             q_next[done] = 0.0

#             indices = np.arrange(self.batch_size)
#             q_target = q_eval[:]

#             q_target[indices, action] = reward + self.gamma*np.max(q_next, axis=1)

#             self.q_eval.train_on_batch(state, q_target)

#             self.epsilon = self.epsilon - self.eps_dec if self.epsilon > self.eps_min else self.eps_min

#             self.learn_step += 1
    
#     def save_models(self):
#         self.q_eval.save(self.q_eval_model_file)
#         self.q_next.save(self.q_target_model_file)
#         print('...saving models...')

#     def load_models(self):
#         self.q_eval = load_model(self.q_eval_model_file)
#         self.q_next = load_model(self.q_target_model_file)
#         print('...loading models...')



# 1 smart AI och 1 dum AI som spelar mot varandra och lär sig
# https://www.youtube.com/watch?v=BSpXCRTOLJA


# # Formatera bakgrund m.m.
# backgroundColor = (201, 255, 229)
# width, height = 500, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Pong demo')
# screen.fill(backgroundColor)
# clock = pygame.time.Clock()

# AIpoints = 0
# playerPoints = 0

# q = pygame.QUIT
# main = True
# Color = (0, 0, 0)
# radius = 5
# game = True

# pygame.init()  # Starta pygame

# # jokerman/cooperblack(badboll), gigi(fantasy), Chopsic.ttf(space), nes(standard)
# font = pygame.font.SysFont("nes", 60)
# btnFont = pygame.font.SysFont("nes", 30)
# # font = pygame.font.Font('Chopsic.ttf', 60)

# winText = font.render("Congratulations!", True, (0, 0, 0))
# lossText = font.render("Game over!", True, (0, 0, 0))
# drawText = font.render("It's a draw!", True, (0, 0, 0))
# btnText = btnFont.render("Try again", True, (255, 255, 255))


# class Ball:
#     def __init__(self, color, width, height):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.draw.circle(
#             screen, (0, 0, 0), (circlePosX, circlePosY), 2*radius)

# # def bounce(x, y, pY, diffX, diffY):
# #     if x == 50:
# #         print('if 1')
# #         if y == pY or y == pY+50:
# #             diffX = -diffX
# #             diffY = -diffY
# #         elif y > pY and y < pY+50:
# #             diffX = -diffX
# #         elif y > pY+50 or y < pY:
# #             if x < 50 and x >= 30:
# #                 diffY = -diffY

# #     elif x == 450:
# #         print('if 2')
# #         if y == pY or y == pY+50:
# #             print('if 2, 1')
# #             diffX = -diffX
# #             diffY = -diffY
# #         elif y > pY and y < pY+50:
# #             print('if 2, 2')
# #             diffX = -diffX
# #         elif y > pY+50 or y < pY:
# #             print('if 2, 3')
# #             if x > 450 and x <= 470:
# #                 diffY = -diffY
# #             else:
# #                 diffX = -diffX
# #     else:
# #         print('else')
# #         diffX = -diffX

# #     print('bounce')
# #     return diffX, diffY


# while main:
#     done = False
#     paddlePosY, AIpaddlePosY = 250, 250
#     direction = 0
#     circlePosX = 250
#     circlePosY = 250 + random.randint(-100, 100)
#     diffX = 0.5
#     diffY = 0.5

#     while game:
#         screen.fill(backgroundColor)
#         pygame.draw.line(screen, (0, 0, 0), (0, 505), (500, 505), 5)
#         player1 = pygame.draw.rect(screen, Color, (30, paddlePosY, 10, 50))
#         # (x kordinat, y kordinat, bredd, längd)
#         AI = pygame.draw.rect(screen, Color, (470, AIpaddlePosY, 10, 50))
#         pygame.draw.line(screen, (0, 0, 0), (249, 0), (249, 600), 2)
#         printPoint = font.render(str(playerPoints), True, (0, 0, 0))
#         printPointAI = font.render(str(AIpoints), True, (0, 0, 0))

#         screen.blit(printPoint, (200 - printPoint.get_width() //
#                                  2, 550 - printPoint.get_height() // 2))
#         screen.blit(printPointAI, (300 - printPointAI.get_width() //
#                                    2, 550 - printPointAI.get_height() // 2))

#         ball = Ball(Color, 5, 5)

#         clock.tick(500)  # Timer för att sakta ner spelet

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#                 main = False

#             if event.type == pygame.KEYDOWN:
#                 if event.key == ord('q'):
#                     pygame.quit()
#                     sys.exit()
#                     main = False

#         if AIpaddlePosY < circlePosY:
#             if AIpaddlePosY > 440:
#                 AIpaddlePosY = 440
#             elif AIpaddlePosY < 10:
#                 AIpaddlePosY = 10
#             else:
#                 AIpaddlePosY += 1

#         elif AIpaddlePosY > circlePosY:
#             if AIpaddlePosY > 440:
#                 AIpaddlePosY = 440
#             elif AIpaddlePosY < 10:
#                 AIpaddlePosY = 10
#             else:
#                 AIpaddlePosY -= 1

#         keys = pygame.key.get_pressed()  # kolla vilka tangenter som trycks ned

#         if keys[pygame.K_w] or keys[pygame.K_UP]:  # vad händer om man trycker på pil upp eller w
#             #förhindrar att paddeln flyger utanför skärmen
#             if paddlePosY > 440:
#                 paddlePosY = 440
#             elif paddlePosY < 10:
#                 paddlePosY = 10
#             else:
#                 direction = -1

#         # vad händer om man trycker på pil ned eller s
#         elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
#             if paddlePosY > 440:
#                 paddlePosY = 440
#             elif paddlePosY < 10:
#                 paddlePosY = 10
#             else:
#                 direction = 1

#         else:
#             direction = 0

#         # Om den krockar med vägg i Y-led
#         if circlePosY >= 500 or circlePosY <= 0:
#             diffY = -diffY

#         # Om den krockar med vänster padel
#         if circlePosX == 50:
#             if circlePosY >= paddlePosY-10 and circlePosY <= paddlePosY+60:
#                 diffX = -diffX  # olika vinklar här

#         # Höger padel
#         elif circlePosX == 450:
#             if circlePosY >= AIpaddlePosY-10 and circlePosY <= AIpaddlePosY+60:
#                 # och här. funktion som gäller för alla diffX = -diffX
#                 diffX = -diffX

#         # Krock med vägg i X-led
#         elif circlePosX == 10 or circlePosX == 490:
#             if playerPoints < 5 and AIpoints < 5:
#                 if circlePosX == 10:
#                     AIpoints += 1
#                 elif circlePosX == 490:
#                     playerPoints += 1
#                 game = False
#             #skriv ut game over över skärmen och avsluta spelet

#         # Addera skillnader till bollens koordinater för förflyttning
#         circlePosX += diffX
#         circlePosY += diffY
#         paddlePosY += direction
#         pygame.display.flip()

#     # Om någon vunnit skriv ut det till player1
#     if AIpoints == 5 or playerPoints == 5:
#         if AIpoints == 5:
#             screen.blit(lossText, (250 - lossText.get_width() //
#                                    2, 250 - lossText.get_height() // 2))

#         elif playerPoints == 5:
#             screen.blit(winText, (250 - winText.get_width() //
#                                   2, 250 - winText.get_height() // 2))

#         else:
#             screen.blit(drawText, (250 - drawText.get_width() //
#                                    2, 250 - drawText.get_height() // 2))

#         button = pygame.draw.rect(screen, (0, 0, 0), (180, 280, 140, 30))
#         screen.blit(btnText, (250 - btnText.get_width() //
#                               2, 295 - btnText.get_height() // 2))
#         pygame.display.flip()

#         # Try again knapp @click
#         while not done:
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == ord('q'):
#                         pygame.quit()
#                         sys.exit()
#                         done = True
#                         main = False

#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     # 1 är vänsterklick, 2 mitten, 3 höger
#                     if event.button == 1:
#                         # `event.pos` är muspekarens position
#                         if button.collidepoint(event.pos):
#                             # Gå ut ur "done" loopen och in i "game" loopen
#                             done = True
#                             game = True

#         # Återställning av poäng om nån vunnit
#         AIpoints = 0
#         playerPoints = 0

#     # Om ingen vunnit hela spelet än men vunnit en omgång
#     else:
#         game = True
