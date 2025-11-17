package com.halo.core_bridge.api.ai.dto;

import java.util.List;

package com.halo.core_bridge.api.ai.dto;

import lombok.*;
import java.util.List;

public class AiDtos {

    @Getter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Request {
        private Long userId;
        private Long resumeId;
        private String summary;
        private List<String> skills;
        private List<RecommendResult> recommendResults;
        private ScoreDetail scoreDetail;
    }

    @Getter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class RecommendResult {
        private String candidateId;   // 예: "65", "test-candidate-001"
        private Double score;
    }

    @Getter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class ScoreDetail {
        private Double cosineSimilarity;
        private Double skillRatio;
        private Double skillScore;
        private Double simScore;
        private Double bonus;
        private Double totalScore;
    }

    @Getter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Response {
        private Long id;
        private Long userId;
        private Long resumeId;
        private String summary;
        private List<String> skills;
        private List<RecommendResult> recommendResults;
        private ScoreDetail scoreDetail;

        @Setter
        private String grade;

        @Setter
        private Boolean isMatched;
    }
}
