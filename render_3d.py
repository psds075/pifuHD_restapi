import pygame
import objloader

# 화면 초기화
pygame.init()
screen = pygame.display.set_mode((512, 512))

# 모델 로드
model = objloader.OBJ(r"test.obj")

# 텍스처 로드
texture = pygame.image.load(r"texture.png")

# 물체 렌더링
for face in model.faces:
    for vertex in face.vertices:
        x, y, z = vertex
        screen.set_at((x, y), texture.get_at((vertex.u, vertex.v)))

# 화면 업데이트
pygame.display.flip()

# 이벤트 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
