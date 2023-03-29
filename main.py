import pygame
import game

WIN = pygame.display.set_mode((game.WIN_width, game.WIN_height))
pygame.display.set_caption("Tetris")
#WIN.fill(game.BLACK)

def main():

    run = True
    shape_change = False
    color_dict = {}
    playground_matrix = game.create_playground(color_dict)
    current_shape = game.get_random_shape()
    next_shape = game.get_random_shape()
    drop_time = 0
    drop_speed = .4

    clock = pygame.time.Clock()



    while run:
        playground_matrix = game.create_playground(color_dict)

        drop_time += clock.get_rawtime()
        clock.tick()

        if drop_time / 1000 > drop_speed:
            drop_time = 0
            current_shape.height += 1
            if not (game.valid_space(current_shape, playground_matrix)) and current_shape.height > 0:
                current_shape.height -= 1
                shape_change = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            current_shape.height += 1
            print("get down")
            if not game.valid_space(current_shape, playground_matrix):
                current_shape.height -= 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

                if event.key == pygame.K_RIGHT:  # Get shape to the right
                    current_shape.width += 1
                    print("go right")
                    if not game.valid_space(current_shape, playground_matrix):
                        current_shape.width -= 1
                
                if event.key == pygame.K_LEFT:  # Get shape to the left
                    current_shape.width -= 1
                    print("go left")
                    if not game.valid_space(current_shape, playground_matrix):
                        current_shape.width += 1
                
                if event.key == pygame.K_UP:  # Change the shape status
                    current_shape.status += 1
                    print("change status")
                    if not game.valid_space(current_shape, playground_matrix):
                        current_shape.status -= 1
                
                # if event.key == pygame.K_DOWN:  # Fall shape
                #     current_shape.height += 1
                #     print("get down")
                #     if not game.valid_space(current_shape, playground_matrix):
                #         current_shape.height -= 1
        
        shape_pos = game.next_shape_status(current_shape)
        for i in range(len(shape_pos)):
            width, height = shape_pos[i]
            if height > -1:
                playground_matrix[height][width] = current_shape.color

        if shape_change:
            #print("TRUE")
            for pos in shape_pos:
                p = (pos[0], pos[1])
                color_dict[p] = current_shape.color
            current_shape = next_shape
            next_shape = game.get_random_shape()
            shape_change = False
            game.handle_full_row(playground_matrix, color_dict)

        game.draw_WIN(WIN, playground_matrix)
        game.display_next_shape(WIN, next_shape)
        pygame.display.update()
        
        if game.is_lost(color_dict):
            run = False
    
    pygame.display.quit()

if __name__ == "__main__":
    main()