<?php

namespace Symfony\Config\Prestashop;

require_once __DIR__.\DIRECTORY_SEPARATOR.'Addons'.\DIRECTORY_SEPARATOR.'CategoriesConfig.php';
require_once __DIR__.\DIRECTORY_SEPARATOR.'Addons'.\DIRECTORY_SEPARATOR.'ApiClientConfig.php';

use Symfony\Component\Config\Definition\Exception\InvalidConfigurationException;

/**
 * This class is automatically generated to help in creating a config.
 */
class AddonsConfig 
{
    private $categories;
    private $apiClient;
    private $_usedProperties = [];

    public function categories(array $value = []): \Symfony\Config\Prestashop\Addons\CategoriesConfig
    {
        $this->_usedProperties['categories'] = true;

        return $this->categories[] = new \Symfony\Config\Prestashop\Addons\CategoriesConfig($value);
    }

    public function apiClient(array $value = []): \Symfony\Config\Prestashop\Addons\ApiClientConfig
    {
        if (null === $this->apiClient) {
            $this->_usedProperties['apiClient'] = true;
            $this->apiClient = new \Symfony\Config\Prestashop\Addons\ApiClientConfig($value);
        } elseif (0 < \func_num_args()) {
            throw new InvalidConfigurationException('The node created by "apiClient()" has already been initialized. You cannot pass values the second time you call apiClient().');
        }

        return $this->apiClient;
    }

    public function __construct(array $value = [])
    {
        if (array_key_exists('categories', $value)) {
            $this->_usedProperties['categories'] = true;
            $this->categories = array_map(fn ($v) => new \Symfony\Config\Prestashop\Addons\CategoriesConfig($v), $value['categories']);
            unset($value['categories']);
        }

        if (array_key_exists('api_client', $value)) {
            $this->_usedProperties['apiClient'] = true;
            $this->apiClient = new \Symfony\Config\Prestashop\Addons\ApiClientConfig($value['api_client']);
            unset($value['api_client']);
        }

        if ([] !== $value) {
            throw new InvalidConfigurationException(sprintf('The following keys are not supported by "%s": ', __CLASS__).implode(', ', array_keys($value)));
        }
    }

    public function toArray(): array
    {
        $output = [];
        if (isset($this->_usedProperties['categories'])) {
            $output['categories'] = array_map(fn ($v) => $v->toArray(), $this->categories);
        }
        if (isset($this->_usedProperties['apiClient'])) {
            $output['api_client'] = $this->apiClient->toArray();
        }

        return $output;
    }

}
