// Copyright 2019 ZTE corporation. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

#include <vector>

#include "dlib/clustering.h"
#include "dlib/rand.h"

namespace ml_runtime {

template <typename SampleType>
struct Kmeans {
  Kmeans(unsigned long n_clusters, long max_iter = 100) : n_clusters(n_clusters), max_iter(max_iter) {
  }

  std::vector<unsigned long> fit(const std::vector<SampleType>& samples) {
    dlib::pick_initial_centers(n_clusters, centers, samples, dlib::linear_kernel<SampleType>());
    dlib::find_clusters_using_kmeans(samples, centers, max_iter);
    if (centers.size() != n_clusters) {
      // should exception process
    }

    std::vector<unsigned long> results(samples.size());
    std::vector<int> hits(centers.size(), 0);
    for (size_t i = 0; i < samples.size(); ++i) {
      size_t best_idx = 0;
      double best_dist = 1e100;
      for (size_t j = 0; j < centers.size(); ++j) {
        auto temp = dlib::length(samples[i] - centers[j]);
        if (temp < best_dist) {
          best_dist = temp;
          best_idx = j;
        }
      }
      results[i] = best_idx;
    }

    return results;
  }

  const std::vector<SampleType>& getCenters() const {
    return centers;
  }

private:
  unsigned long n_clusters;
  long max_iter = 100;
  std::vector<SampleType> centers;
};

}  // namespace ml_runtime
